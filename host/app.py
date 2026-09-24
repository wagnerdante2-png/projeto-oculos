from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field


ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"

app = FastAPI(title="Projeto Óculos Host", version="0.1.0")


@dataclass
class DeviceSession:
    device_id: str
    websocket: WebSocket
    capabilities: set[str] = field(default_factory=set)
    firmware: str | None = None
    connected_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    last_seen: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    telemetry: dict[str, Any] = field(default_factory=dict)


class HudCommand(BaseModel):
    text: str = Field(min_length=1, max_length=240)
    ttl_ms: int = Field(default=5000, ge=250, le=60000)


class Hub:
    def __init__(self) -> None:
        self.devices: dict[str, DeviceSession] = {}
        self.ui_clients: set[WebSocket] = set()
        self._lock = asyncio.Lock()

    async def snapshot(self) -> list[dict[str, Any]]:
        async with self._lock:
            return [
                {
                    "device_id": d.device_id,
                    "capabilities": sorted(d.capabilities),
                    "firmware": d.firmware,
                    "connected_at": d.connected_at,
                    "last_seen": d.last_seen,
                    "telemetry": d.telemetry,
                }
                for d in self.devices.values()
            ]

    async def broadcast_ui(self, event: dict[str, Any]) -> None:
        stale: list[WebSocket] = []
        for ws in list(self.ui_clients):
            try:
                await ws.send_json(event)
            except Exception:
                stale.append(ws)
        for ws in stale:
            self.ui_clients.discard(ws)

    async def broadcast_snapshot(self) -> None:
        await self.broadcast_ui({"type": "snapshot", "devices": await self.snapshot()})


hub = Hub()


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(STATIC / "index.html")


@app.get("/api/health")
async def health() -> dict[str, Any]:
    return {"ok": True, "service": "projeto-oculos-host", "devices": len(hub.devices)}


@app.get("/api/devices")
async def devices() -> list[dict[str, Any]]:
    return await hub.snapshot()


@app.post("/api/devices/{device_id}/hud")
async def send_hud(device_id: str, command: HudCommand) -> dict[str, Any]:
    session = hub.devices.get(device_id)
    if not session:
        raise HTTPException(status_code=404, detail="device offline")
    if "hud.text" not in session.capabilities:
        raise HTTPException(status_code=409, detail="device does not advertise hud.text")

    payload = {
        "type": "command",
        "command": "hud.text",
        "id": f"hud-{int(datetime.now(timezone.utc).timestamp() * 1000)}",
        "payload": {"text": command.text, "ttl_ms": command.ttl_ms},
    }
    await session.websocket.send_json(payload)
    return {"queued": True, "device_id": device_id, "command": payload}


@app.websocket("/ws/ui")
async def ui_ws(websocket: WebSocket) -> None:
    await websocket.accept()
    hub.ui_clients.add(websocket)
    await websocket.send_json({"type": "snapshot", "devices": await hub.snapshot()})
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        hub.ui_clients.discard(websocket)


@app.websocket("/ws/glasses/{device_id}")
async def glasses_ws(websocket: WebSocket, device_id: str) -> None:
    await websocket.accept()
    session = DeviceSession(device_id=device_id, websocket=websocket)
    async with hub._lock:
        old = hub.devices.get(device_id)
        if old:
            try:
                await old.websocket.close(code=4001, reason="replaced by newer session")
            except Exception:
                pass
        hub.devices[device_id] = session
    await hub.broadcast_snapshot()

    try:
        while True:
            raw = await websocket.receive_text()
            message = json.loads(raw)
            session.last_seen = datetime.now(timezone.utc).isoformat()

            msg_type = message.get("type")
            if msg_type == "hello":
                session.capabilities = set(message.get("capabilities", []))
                session.firmware = message.get("firmware")
                await websocket.send_json({
                    "type": "hello_ack",
                    "server_time": datetime.now(timezone.utc).isoformat(),
                    "protocol": "0.1",
                })
            elif msg_type == "telemetry":
                session.telemetry.update(message.get("payload", {}))
            elif msg_type in {"ack", "event", "imu"}:
                await hub.broadcast_ui({"type": "device_event", "device_id": device_id, "message": message})
            else:
                await websocket.send_json({"type": "error", "code": "unsupported_message", "received": msg_type})

            await hub.broadcast_snapshot()
    except (WebSocketDisconnect, json.JSONDecodeError):
        pass
    finally:
        async with hub._lock:
            if hub.devices.get(device_id) is session:
                hub.devices.pop(device_id, None)
        await hub.broadcast_snapshot()
