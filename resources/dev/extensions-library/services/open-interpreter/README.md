# Open Interpreter

A local LLM that can run code on your computer.

## What is Open Interpreter?

Open Interpreter lets LLMs run code locally (Python, JavaScript, Shell, etc.). It provides:
- A ChatGPT-like interface in your terminal
- Browser control for research tasks
- File creation and editing
- Data analysis and visualization

## Configuration

The service connects to your local LLM via `${LLM_API_URL}` (default: `http://llama-server:8000`).

## Usage

### Via API

Once running, access the API at `http://localhost:<port>`:

```bash
# Health check
curl http://localhost:8080/health

# Chat (non-streaming)
curl -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What OS are we running?", "stream": false}'

# Chat (streaming)
curl http://localhost:8080/chat/stream \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"message": "Plot AAPL stock price", "stream": true}'
```

### Via Terminal (CLI)

```bash
# Run interpreter interactively
docker compose run --rm open-interpreter

# Run a single command
docker compose run --rm open-interpreter -y "Create a file called test.txt"
```

## Data Persistence

Data is stored in `./data/open-interpreter/`:

- Chat history
- Config files
- Generated files

## Ports

| Environment Variable | Default | Description |
|---------------------|---------|-------------|
| `OPEN_INTERPRETER_PORT` | `8080` | API server port |
| `LLM_API_URL` | `http://llama-server:8000` | Your local LLM endpoint |

## Features

| Feature | Description |
|---------|-------------|
| Code Execution | Run Python, JavaScript, Shell code locally |
| Browser Control | Control Chrome for web research |
| File Operations | Create/edit files, images, videos, PDFs |
| Data Analysis | Plot, clean, and analyze datasets |

## Notes

- No GPU required for basic usage
- Browser automation needs Chrome installed on host
- Code runs with `auto_run=True` by default (no manual approval)
