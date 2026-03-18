# Fooocus Extension

**Fooocus** is a user-friendly image generation UI built on top of Automatic1111. It provides an intuitive interface for generating high-quality images using Stable Diffusion.

## Extension Info

| Property | Value |
|----------|-------|
| **ID** | fooocus |
| **Container Name** | dream-fooocus |
| **Default Port** | 7865 |
| **GPU Support** | AMD, NVIDIA |
| **Depends On** | None (standalone) |
| **Category** | Optional |

## What It Does

Fooocus provides a simple, beautiful interface for generating AI images. It's designed to be easy to use while still offering powerful features like:

- Text-to-image generation
- Image-to-image generation
- Advanced controlnet integration
- Multiple sampling methods
- High-resolution upscaling

## Configuration

Fooocus uses sensible defaults. No manual configuration needed.

## Usage

1. Enable the extension: `dream extensions enable fooocus`
2. Access the UI at `http://localhost:7865`
3. Start generating images with natural language prompts

## Integration

Fooocus runs as a standalone image generation service. It does not connect to Dream Server's LLM endpoint since it's purely an image generation tool.

## Uninstall

Disable the extension: `dream extensions disable fooocus`

This will remove the container but preserve your generated images in `./data/fooocus/`.
