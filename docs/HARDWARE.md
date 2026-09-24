# Estratégia de hardware

## MVP A - Sensor clip / haste inteligente

Primeiro alvo recomendado:

- Seeed Studio XIAO ESP32-S3 Sense;
- câmera e microfone do módulo Sense;
- bateria LiPo pequena com proteção;
- estrutura clip-on ou haste substituível impressa em 3D;
- saída de áudio inicialmente pelo cyberdeck/fone Bluetooth, para reduzir complexidade;
- HUD opcional em uma segunda iteração do mesmo MVP.

A escolha segue a mesma classe de hardware usada por projetos atuais como OpenGlass/OpenSQZ e SidekickOS, mas o software deste repositório será próprio.

## MVP B - HUD monocular

Adicionar:

- microdisplay ou módulo óptico monocular;
- driver apropriado ao display;
- combinador/freeform/birdbath conforme módulo escolhido;
- capability `hud.text` e depois `hud.bitmap`.

Objetivo: texto, ícones, setas, tradução, checklist e resposta de IA. Isso é HUD; não exige SLAM.

## MVP C - Áudio integrado

- microfone(s) digital(is);
- codec/amp de baixo consumo;
- transdutor de condução óssea ou pequeno alto-falante direcional;
- cancelamento/controle de eco no host ou firmware conforme capacidade.

## MVP D - Tracking

- IMU de 6 eixos com timestamps confiáveis;
- câmera com calibração estável;
- sincronização temporal câmera/IMU;
- 3DoF antes de 6DoF.

## AR espacial

Para objetos virtuais ancorados no mundo, o sistema precisará de VIO/SLAM e de óptica/display com calibração adequada. Esta fase deve ser tratada como subsistema XR independente, potencialmente usando Monado/OpenXR e algoritmos externos.

## Regra mecânica

Evitar depender de armação totalmente impressa no primeiro protótipo. Preferir:

1. clip-on em armação comercial; ou
2. frente comercial + hastes/modulos impressos.

Isso reduz risco de quebra, peso e retrabalho ergonômico.
