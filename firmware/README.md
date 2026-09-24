# Firmware

Alvo inicial planejado: **Seeed Studio XIAO ESP32-S3 Sense / ESP-IDF**.

Ainda não há firmware de produção neste diretório. A primeira implementação deverá seguir o protocolo de `docs/PROTOCOL.md` e cumprir, nesta ordem:

1. provisionamento local seguro;
2. `hello` + capability advertisement;
3. telemetria;
4. snapshot de câmera;
5. botão/LED de privacidade;
6. áudio;
7. HUD.

Não serão adicionadas chaves de API, senhas Wi-Fi ou IPs privados ao repositório.
