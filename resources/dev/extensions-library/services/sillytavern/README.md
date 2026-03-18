# SillyTavern Extension for Dream Server

## Overview

SillyTavern is a character/roleplay chat UI that connects to local LLMs. This extension provides a dedicated instance integrated with Dream Server's stack.

## Features

- Runs SillyTavern with local LLM integration
- GPU acceleration (NVIDIA/AMD)
- Persistent storage for character files and conversations
- Health endpoint at `/`

## Usage

### Enable the extension

```bash
dream extensions enable sillytavern
```

### Access the UI

```
http://localhost:${SILLYTAVERN_PORT:-8080}
```

### Configure

Edit `.env`:

```
SILLYTAVERN_API_URL=http://llama-server:8080/v1
```

Restart to apply:

```bash
docker compose down sillytavern && docker compose up -d sillytavern
```

## Integration

SillyTavern works with:
- **llama-server** — Primary LLM backend
- **n8n workflows** — Trigger roleplay sessions via webhook

## Uninstall

```bash
dream extensions disable sillytavern
```

Character files in `./data/sillytavern/` are preserved.
