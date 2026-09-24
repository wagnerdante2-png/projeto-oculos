# Roadmap

## M0 - Arquitetura e simulador — iniciado

- protocolo v0.1;
- host executável;
- painel de telemetria;
- simulador;
- HUD command/ACK.

## M1 - Primeiro hardware

- fechar BOM do XIAO ESP32-S3 Sense;
- firmware de descoberta/provisionamento;
- câmera snapshot;
- telemetria de bateria;
- botão físico e indicador de captura.

**Critério de saída:** óculos envia imagem real ao host e recebe comando sem cabo USB.

## M2 - Áudio bidirecional

- captura de microfone;
- streaming eficiente;
- ASR local no host;
- TTS/áudio de retorno;
- medição de latência.

**Critério de saída:** pergunta por voz -> processamento no host -> resposta audível.

## M3 - HUD monocular

- escolher módulo óptico/display;
- driver;
- texto e ícones;
- brilho e timeout;
- teleprompter/tradução/checklist.

**Critério de saída:** resposta do host exibida no campo visual com leitura confortável.

## M4 - Integração cyberdeck

- descoberta automática;
- serviço inicia com o sistema;
- bateria/qualidade de conexão no painel do cyberdeck;
- perfis local/cloud;
- operação offline básica.

## M5 - Tracking 3DoF / IMU

- IMU calibrada;
- timestamps;
- orientação da cabeça;
- HUD estabilizado por orientação quando útil.

## M6 - AR espacial 6DoF

- câmera estéreo/depth ou configuração VIO viável;
- SLAM/VIO como processo externo;
- OpenXR/Monado;
- calibração óptica;
- objetos ancorados no ambiente.

## M7 - Hardware próprio

Somente depois de validar ergonomia, consumo e fluxo de uso:

- PCB própria;
- hastes customizadas;
- bateria dividida;
- áudio integrado;
- industrialização do conjunto.
