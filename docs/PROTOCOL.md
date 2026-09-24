# Protocolo v0.1

Envelope JSON via WebSocket para controle e telemetria. Fluxos binários de câmera/áudio serão especificados separadamente para não forçar Base64 no canal de eventos.

## Hello

```json
{
  "type": "hello",
  "firmware": "xiao-s3/0.1.0",
  "capabilities": ["camera.capture", "mic.stream", "hud.text"]
}
```

## Telemetria

```json
{
  "type": "telemetry",
  "payload": {
    "battery_pct": 87.4,
    "rssi_dbm": -51,
    "temperature_c": 33.2,
    "uptime_s": 428
  }
}
```

## Comando HUD

```json
{
  "type": "command",
  "command": "hud.text",
  "id": "hud-123",
  "payload": {"text": "Porta 3 à esquerda", "ttl_ms": 5000}
}
```

## ACK

```json
{"type":"ack","command_id":"hud-123","ok":true}
```

## Evolução prevista

- autenticação mútua entre óculos e host;
- `session_id` e sequência monotônica;
- sincronização de relógio para câmera + IMU;
- envelopes CBOR para reduzir overhead;
- WebRTC/RTP para mídia em tempo real;
- QoS separado para áudio, vídeo, IMU e comandos.
