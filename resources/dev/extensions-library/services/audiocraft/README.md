# AudioCraft Extension

AI music and sound effect generation by Meta.

## Description

AudioCraft is a PyTorch library for deep learning research on audio generation. It features:

- **MusicGen**: A state-of-the-art controllable music generation model
- **AudioGen**: A text-to-sound effect generation model
- **EnCodec**: High-quality neural audio codec

## Features

- **Text-to-Music**: Generate music from text descriptions
- **Text-to-Sound**: Create sound effects from text prompts
- **Local Processing**: All generation happens on your GPU
- **Gradio UI**: Easy-to-use web interface

## GPU Requirements

- **Minimum**: 6GB VRAM (NVIDIA)
- **Recommended**: 8GB+ VRAM for larger models

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `AUDIOCRAFT_PORT` | 7860 | External port for the UI |
| `AUDIOCRAFT_HOST` | audiocraft | Hostname for service discovery |

## Data Persistence

- `./data/audiocraft/` - Generated audio files
- `./data/audiocraft/models/` - Downloaded model weights

## Usage

1. Enable the extension in the Dream Dashboard
2. Access the UI at `http://localhost:7860`
3. Use the MusicGen tab to generate music
4. Use the AudioGen tab to generate sound effects

## Model Information

- **MusicGen Small**: 300M parameters, fastest generation
- **AudioGen Medium**: 1B parameters, high-quality sound effects

Models are downloaded automatically on first use.

## Upstream

- **GitHub**: https://github.com/facebookresearch/audiocraft
- **Paper**: https://arxiv.org/abs/2306.05284
- **License**: MIT (code), CC BY-NC 4.0 (models - non-commercial)

## Note on Model Licensing

The AudioCraft models are released under CC BY-NC 4.0 (non-commercial use only).
Please review the license terms before using generated content commercially.
