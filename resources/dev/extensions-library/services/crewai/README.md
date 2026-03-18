# CrewAI Studio

No-code multi-agent AI workflow builder.

## Features

- **Visual crew builder**: Create agents and tasks through UI
- **Local LLM support**: Works with Dream Server's local models
- **Multi-provider**: OpenAI, Ollama, LM Studio, Groq, Anthropic
- **Export**: Save crews as standalone Streamlit apps

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `CREWAI_HOST` | `crewai` | Hostname for service |
| `CREWAI_PORT` | `8501` | External port for UI |
| `LLM_API_URL` | (from env) | Dream Server LLM endpoint |
| `OPENAI_API_KEY` | `dream-local` | API key for local LLM |

## Usage

1. Start the service: `docker compose up -d`
2. Access at `http://localhost:8501`
3. Create agents, define tasks, and run crews

## Data Persistence

- Crew configurations and history: `./data/crewai/`

## Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [CrewAI-Studio GitHub](https://github.com/strnad/CrewAI-Studio)
