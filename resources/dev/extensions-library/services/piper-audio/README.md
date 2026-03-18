# Piper TTS Extension for Dream Server

## Overview

Piper is a fast, local neural text-to-speech system that sounds great and is optimized for edge devices including Raspberry Pi 4. It uses the Wyoming protocol for integration.

## Features

- Local neural TTS (no cloud dependency)
- Multiple voice models available
- Low latency, optimized for edge
- Wyoming protocol support
- CPU-based (no GPU required)

## Usage

### Enable the extension

```bash
dream extensions enable piper-audio
```

### Wyoming Protocol Endpoint

```
tcp://localhost:${PIPER_PORT:-10200}
```

### HTTP API (if supported by voice pipeline)

Check your voice pipeline configuration for HTTP endpoints.

## Configuration

| Environment Variable | Default | Description |
|---------------------|---------|-------------|
| `PIPER_PORT` | 10200 | Wyoming protocol port |
| `PIPER_VOICE` | en_US-lessac-medium | Default voice model |
| `PIPER_LENGTH` | 1.0 | Speech speed (0.5-2.0) |
| `PIPER_NOISE` | 0.667 | Noise scale (0.0-1.0) |
| `PIPER_NOISEW` | 0.333 | Noise width (0.0-1.0) |
| `PIPER_SPEAKER` | 0 | Speaker ID for multi-speaker voices |
| `PIPER_PROCS` | 1 | Number of worker processes |

### Available Voices

Popular voices include:
- `en_US-lessac-medium` (default, high quality)
- `en_US-lessac-low` (faster, lower quality)
- `en_US-amy-medium`
- `en_GB-southern_english_male-medium`

Full list: <https://huggingface.co/rhasspy/piper-voices/tree/main>

## Integration

Piper integrates with:
- **Home Assistant** — Via Wyoming protocol
- **Open WebUI** — Voice output for chat responses
- **n8n workflows** — TTS automation nodes

## Uninstall

```bash
dream extensions disable piper-audio
```

Voice models in `./data/piper/` are preserved.
