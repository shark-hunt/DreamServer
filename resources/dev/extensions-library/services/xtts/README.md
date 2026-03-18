# XTTS (Coqui TTS)

High-quality multilingual text-to-speech with voice cloning.

## Features

- **Voice cloning**: Clone voices from short samples
- **Multilingual**: Support for 17 languages
- **Streaming**: Real-time TTS generation
- **GPU acceleration**: CUDA support for fast inference

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `XTTS_HOST` | `xtts` | Hostname for service |
| `XTTS_PORT` | `8100` | External port for API |

## Usage

1. Start the service: `docker compose up -d`
2. API available at `http://localhost:8100`
3. Send POST requests to `/tts` with text and speaker audio

## Example Request

```bash
curl -X POST http://localhost:8100/tts \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, this is a test.",
    "speaker_wav": "speaker.wav",
    "language": "en"
  }'
```

## Data Persistence

- TTS models cached in `./data/xtts/`

## Resources

- [XTTS Documentation](https://docs.coqui.ai/en/latest/models/xtts.html)
- [GitHub](https://github.com/coqui-ai/TTS)
