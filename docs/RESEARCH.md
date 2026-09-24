# Pesquisa de referências públicas — 24/09/2026

Este documento registra referências técnicas, não código incorporado.

## Referências principais

### [OpenSQZ/OpenGlass](https://github.com/OpenSQZ/OpenGlass)

Arquitetura 2026 muito alinhada ao projeto: ESP32-S3 no wearable e inferência multimodal local em um computador próximo. Publica firmware de câmera/PDM, host bridge, CAD/3MF/BOM e ferramentas de avaliação. Apache-2.0.

Uso no nosso projeto: **referência arquitetural primária** para a separação sensing/computing.

### [siersidekick/SidekickOS](https://github.com/siersidekick/SidekickOS)

Clip-on baseado em XIAO ESP32-S3 Sense, com firmware ESP-IDF, cliente Python/Web e arquivos STEP/STL/3MF.

Uso: referência forte para mecânica modular e bring-up do XIAO.

### [nickjizheng/Visionbridge-AI-Glasses](https://github.com/nickjizheng/Visionbridge-AI-Glasses)

Firmware ESP32 com câmera, microfone, speaker, display, WebSocket/MQTT/UDP, OPUS e organização por placas. MIT.

Uso: referência para arquitetura de firmware e separação por board adapters.

### [Mentra-Community/MentraOS](https://github.com/Mentra-Community/MentraOS)

Sistema aberto para múltiplos óculos comerciais, com abstração de câmera/mic/display/speaker e apps. Apache-2.0.

Uso: referência para o nosso **modelo de capacidades**; não será dependência obrigatória do MVP próprio.

### [brilliantlabsAR/frame-codebase](https://github.com/brilliantlabsAR/frame-codebase)

Código completo do Brilliant Labs Frame: nRF52 para operação/Bluetooth/energia e FPGA para aceleração de câmera/gráficos.

Uso: referência de longo prazo para hardware muito mais integrado e de baixo consumo.

### [RR-CREATOR/GLARE](https://github.com/RR-CREATOR/GLARE)

Projeto maker com ESP32-S3, dois microfones, câmera, gyro/GPS e HUD birdbath com microdisplay.

Uso: referência para fase HUD óptico barato.

### [Mentra-Community/OpenSourceSmartGlasses](https://github.com/Mentra-Community/OpenSourceSmartGlasses)

Projeto histórico com ESP32, display, microfone, PCB e armação impressa. Evoluiu para a linha AugmentOS/MentraOS.

Uso: aprender com a evolução: começar simples, útil e vestível antes de adicionar compute pesado.

### [Leap Motion / Project North Star](https://github.com/leapmotion/ProjectNorthStar) + [comunidade](https://github.com/projectnorthstar)

Headset AR óptico open-source com mecânica, eletrônica, software e calibração; comunidade documenta Northstar Next e variações mais recentes.

Uso: referência para **AR espacial**, não para o primeiro MVP. O repositório original é GPL-3.0, portanto não copiar código para o núcleo permissivo.

### [Monado](https://gitlab.freedesktop.org/monado/monado)

Runtime OpenXR aberto e conformante, com suporte a Linux/Android/Windows e histórico de suporte ao North Star.

Uso: candidato para a camada XR futura, executada no cyberdeck/host.

### [OpenVINS](https://github.com/rpng/open_vins) / [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3)

Soluções conhecidas para VIO/SLAM. São úteis na fase de tracking, mas possuem implicações de licença (GPL em projetos relevantes) e custo computacional.

Uso: integração externa experimental, nunca pressuposto do MVP.

## Conclusões técnicas

1. **Bluetooth sozinho não é a escolha correta para vídeo contínuo.** BLE deve ficar em provisionamento, descoberta e comandos leves; Wi-Fi/WebRTC/RTP/WebSocket cobre mídia e telemetria conforme a fase.
2. **ESP32-S3 é suficiente como sensor/periférico**, não como cérebro de IA/AR.
3. **HUD e AR não são a mesma coisa.** Texto fixo no campo visual é muito mais simples e já entrega valor.
4. **AR espacial exige tracking e calibração**, não apenas “projetar uma imagem na lente”.
5. **A melhor primeira mecânica é modular**, clip-on ou hastes customizadas sobre frente comercial.
6. **O cyberdeck é uma vantagem**, pois permite mais bateria, compute, refrigeração e evolução sem aumentar o peso do óculos.
7. O protocolo deve ser nosso e agnóstico ao hardware para permitir troca de ESP32 por Linux embarcado sem reescrever os serviços de IA.
