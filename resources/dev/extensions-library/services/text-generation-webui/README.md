# Text Generation WebUI (Oobabooga)

The most feature-complete local LLM inference UI. Supports GGUF, GPTQ, AWQ, EXL2, and HF transformer model formats with an intuitive chat interface and powerful API server.

## What It Does

- Load and run local models in GGUF, GPTQ, AWQ, EXL2, and HF transformer formats
- Chat and instruct modes with character support
- OpenAI-compatible API on port 5001 (drop-in replacement for OpenAI clients)
- Built-in extensions: Whisper STT, Silero TTS, Superbooga, and more
- LoRA adapter loading and merging
- Fine-grained generation parameter control (temperature, repetition penalty, samplers, etc.)

## Quick Start

```bash
dream extensions enable text-generation-webui
```

Then open **http://localhost:7862** and load a model via the Model tab.

## Loading Models

Place GGUF or other model files in `./data/text-generation-webui/models/` and refresh the model list in the UI. Alternatively, download directly from the Model tab using a Hugging Face repo ID.

## API Usage

The OpenAI-compatible API runs on port 5001:

```bash
curl http://localhost:5001/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "your-model", "messages": [{"role": "user", "content": "Hello!"}]}'
```

## GPU Notes

- **NVIDIA:** Uses the `default-nvidia-v4.0` image with CUDA support
- **AMD:** Swap the image tag to `default-rocm-v4.0` in compose.yaml
- **CPU-only:** Swap to `default-cpu-v4.0` (no GPU block needed in deploy section)

## Data Persistence

All user data is stored under `./data/text-generation-webui/`:
- `models/` — downloaded model files
- `characters/` — custom character cards
- `presets/` — generation presets
- `loras/` — LoRA adapters
- `logs/` — conversation logs
