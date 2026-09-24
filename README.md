# Projeto Óculos

MVP modular de óculos inteligentes complementar ao futuro cyberdeck.

## Objetivo

Separar o dispositivo vestível do processamento pesado:

- **Óculos**: câmera, microfone, IMU, áudio, HUD/display e energia.
- **Cyberdeck/host**: visão computacional, fala, IA, memória, regras e futura camada AR/OpenXR.
- **Transporte**: Wi-Fi para mídia/telemetria de maior banda e BLE para descoberta, provisionamento e comandos leves.

O projeto começa com um simulador para validar o protocolo e a arquitetura antes de travar o hardware definitivo.

## Estado atual

**M0 - Bootstrap executável**

- host FastAPI com WebSocket;
- registro de dispositivos por capacidades;
- painel web de diagnóstico;
- simulador de óculos;
- comando HUD host -> óculos e ACK;
- documentação de arquitetura, pesquisa, hardware e roadmap.

## Executar no Codespaces/Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r host/requirements.txt
uvicorn host.app:app --host 0.0.0.0 --port 8000
```

Abra a porta 8000. Em outro terminal:

```bash
source .venv/bin/activate
python simulator/mock_glasses.py
```

O dispositivo `mock-001` aparecerá no painel. Envie um texto pelo botão **Enviar HUD** para testar o caminho host -> óculos -> ACK.

## Princípios

1. Local-first sempre que viável.
2. Nenhuma chave de API embutida no firmware.
3. Hardware desacoplado por capacidades, não por fabricante.
4. Wi-Fi para vídeo/áudio; BLE não será tratado como canal principal de streaming.
5. HUD e AR espacial são camadas diferentes.
6. Projetos GPL ficam como integrações externas; código copyleft não será copiado para o núcleo permissivo.
7. Indicadores claros de câmera/microfone e controles de privacidade fazem parte do produto, não são pós-requisitos.

## Documentação

- [Pesquisa de referências](docs/RESEARCH.md)
- [Arquitetura](docs/ARCHITECTURE.md)
- [Hardware](docs/HARDWARE.md)
- [Protocolo](docs/PROTOCOL.md)
- [Roadmap](docs/ROADMAP.md)

## Licença

Código original deste repositório: Apache-2.0. Dependências e projetos de referência mantêm suas próprias licenças.
