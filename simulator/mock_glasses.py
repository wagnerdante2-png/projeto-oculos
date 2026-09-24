from __future__ import annotations

import asyncio
import json
import random
import time

import websockets


DEVICE_ID = "mock-001"
URI = f"ws://127.0.0.1:8000/ws/glasses/{DEVICE_ID}"


async def telemetry(ws: websockets.ClientConnection) -> None:
    started = time.monotonic()
    battery = 94.0
    while True:
        battery = max(0.0, battery - 0.02)
        await ws.send(json.dumps({
            "type": "telemetry",
            "payload": {
                "battery_pct": round(battery, 1),
                "rssi_dbm": random.randint(-62, -43),
                "temperature_c": round(random.uniform(31.5, 34.5), 1),
                "uptime_s": int(time.monotonic() - started),
            },
        }))
        await asyncio.sleep(2)


async def main() -> None:
    async with websockets.connect(URI, ping_interval=20, ping_timeout=20) as ws:
        await ws.send(json.dumps({
            "type": "hello",
            "firmware": "mock/0.1.0",
            "capabilities": [
                "camera.capture",
                "mic.stream",
                "speaker.play",
                "hud.text",
                "imu.6dof",
                "telemetry.power",
            ],
        }))
        print("connected:", await ws.recv())

        telemetry_task = asyncio.create_task(telemetry(ws))
        try:
            async for raw in ws:
                msg = json.loads(raw)
                if msg.get("type") == "command" and msg.get("command") == "hud.text":
                    payload = msg.get("payload", {})
                    print(f"HUD <= {payload.get('text')} ({payload.get('ttl_ms')} ms)")
                    await ws.send(json.dumps({
                        "type": "ack",
                        "command_id": msg.get("id"),
                        "ok": True,
                    }))
        finally:
            telemetry_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
