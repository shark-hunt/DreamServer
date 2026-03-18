# Continue (AI Coding Assistant)

Open-source AI coding assistant for VS Code and JetBrains IDEs.

## Features

- **IDE integration**: Native extensions for VS Code and JetBrains
- **Local LLM support**: Uses Dream Server's local models
- **Code completion**: Inline suggestions and chat
- **Privacy**: Code never leaves your machine

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `CONTINUE_HOST` | `continue` | Hostname for service |
| `CONTINUE_PORT` | `8890` | External port for config server |
| `LLM_API_URL` | (from env) | Dream Server LLM endpoint |

## Usage

1. Start the service: `docker compose up -d`
2. Install Continue extension in your IDE
3. Configure IDE to use `http://<dream-server>:8890` as remote config server
4. Or manually set the API base URL to Dream Server's LLM endpoint

## Data Persistence

- Config and history: `./data/continue/`

## Resources

- [Continue Documentation](https://docs.continue.dev/)
- [GitHub](https://github.com/continuedev/continue)
