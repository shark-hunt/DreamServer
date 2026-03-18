# InvokeAI Extension

Professional-grade image generation with Stable Diffusion.

## Description

InvokeAI is a leading creative engine for Stable Diffusion models, empowering professionals, artists, and enthusiasts to generate and create visual media using the latest AI-driven technologies.

## Features

- **Image Generation**: State-of-the-art Stable Diffusion with FLUX model support
- **Node Canvas**: Visual workflow builder for complex image pipelines
- **Control Layers**: ControlNet and Control LoRA for precise image control
- **Layer Support**: Non-destructive editing with full layer management
- **Professional UI**: Best-in-class interface for serious creators

## GPU Requirements

- **Minimum**: 8GB VRAM (NVIDIA or AMD)
- **Recommended**: 12GB+ VRAM for FLUX models
- **Optimal**: 24GB+ VRAM for maximum flexibility

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `INVOKEAI_PORT` | 9090 | External port for the UI |
| `INVOKEAI_HOST` | invokeai | Hostname for service discovery |

## Data Persistence

All data is stored in `./data/invokeai/`:
- Models and checkpoints
- Configuration files
- Generated outputs

## Usage

1. Enable the extension in the Dream Dashboard
2. Access the UI at `http://localhost:9090`
3. Install models through the Model Manager
4. Start generating images

## Upstream

- **Website**: https://invoke.ai
- **Documentation**: https://invoke-ai.github.io/InvokeAI/
- **GitHub**: https://github.com/invoke-ai/InvokeAI
- **License**: Apache 2.0
