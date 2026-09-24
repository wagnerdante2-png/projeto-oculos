# Arquitetura alvo

## Decisão principal

O óculos não será o computador principal. Ele será um **periférico sensorial e de apresentação**, enquanto o cyberdeck/host executa processamento pesado.

```text
[ ÓCULOS ]
 câmera | mic | IMU | HUD | áudio | bateria
        |  Wi‑Fi: mídia/telemetria
        |  BLE: descoberta/provisionamento/controle leve
        v
[ COMPANION CORE / CYBERDECK ]
 gateway -> eventos -> percepção -> raciocínio -> resposta -> HUD/áudio
                     |                 |
                     +-> VIO/SLAM      +-> ferramentas locais
                     +-> visão/ASR     +-> memória opcional
                     +-> OpenXR futuro
```

## Por que esta divisão

- reduz peso e calor no rosto;
- aumenta autonomia;
- permite trocar o processador do cyberdeck sem redesenhar o óculos;
- permite começar com ESP32-S3 e migrar para Linux embarcado somente se necessário;
- favorece IA local e privacidade;
- deixa AR espacial como extensão, não como requisito do primeiro protótipo.

## Camadas

### 1. Device layer

Drivers e firmware específicos: XIAO ESP32-S3 Sense inicialmente; RV1106 e outros no futuro.

### 2. Transport layer

- Wi-Fi/WebSocket: comandos, telemetria e eventos.
- Wi-Fi/HTTP, RTP ou WebRTC: imagem/áudio contínuo em fases posteriores.
- BLE: descoberta e bootstrap de rede.

### 3. Capability model

O host descobre funcionalidades anunciadas pelo dispositivo, por exemplo:

- `camera.capture`
- `camera.stream`
- `mic.stream`
- `speaker.play`
- `hud.text`
- `hud.bitmap`
- `imu.6dof`
- `telemetry.power`

Assim o mesmo host poderá conversar com protótipos diferentes sem condicionais espalhados pelo sistema.

### 4. Perception/services

Plugins independentes para ASR, visão, OCR, tradução, TTS, detecção e, futuramente, VIO/SLAM.

### 5. XR layer

OpenXR/Monado entra somente quando houver hardware de tracking e display adequados. O núcleo não depende dessa camada.

## Privacidade e segurança

- nenhuma credencial de serviço deve ficar gravada em código versionado;
- câmera/microfone precisam de indicador perceptível e controle físico ou lógico explícito;
- gravação persistente é opt-in;
- processamento local é preferido quando o cyberdeck comportar;
- logs de desenvolvimento não devem armazenar áudio/imagens por padrão.
