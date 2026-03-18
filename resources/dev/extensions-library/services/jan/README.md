# Jan

A ChatGPT alternative that runs 100% offline on your computer.

## Features

- **Local-first**: All data stays on your machine
- **Multi-engine support**: llama.cpp, TensorRT-LLM
- **Privacy-focused**: No cloud dependency
- **Model management**: Built-in model downloader and manager

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `JAN_HOST` | `jan` | Hostname for Jan service |
| `JAN_PORT` | `1337` | External port for Jan UI |

## Usage

1. Start the service: `docker compose up -d`
2. Access at `http://localhost:1337`
3. Download models through the UI or place them in `./data/jan/models/`

## Data Persistence

- Models and conversations stored in `./data/jan/`

## Resources

- [Jan Documentation](https://jan.ai/docs)
- [GitHub](https://github.com/janhq/jan)
