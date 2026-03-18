# Flowise Extension

Visual LLM workflow builder for Dream Server.

## What It Is

Flowise is a drag-and-drop tool to build LLM workflows:
- Visual node editor for AI pipelines
- 100+ pre-built integrations
- Build chatbots, agents, and automation
- Export as API endpoints
- No coding required

## Features

- **Visual builder**: Drag-and-drop node editor
- **LLM support**: OpenAI, Anthropic, Azure, local models
- **RAG workflows**: Document loaders, chunkers, vector DBs
- **Agent building**: Tools, memory, decision-making
- **Integrations**: Slack, Discord, databases, APIs
- **API export**: Deploy flows as REST endpoints
- **Chatflows**: Conversational AI builders

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLOWISE_PORT` | External port | `3002` |
| `FLOWISE_USERNAME` | Admin username | (none) |
| `FLOWISE_PASSWORD` | Admin password | (none) |
| `FLOWISE_SECRETKEY_OVERWRITE` | Encryption key | (auto-generated) |
| `FLOWISE_DISABLE_TELEMETRY` | Disable analytics | `true` |

### Authentication (Optional)

To require login:
```bash
# In your .env
FLOWISE_USERNAME=admin
FLOWISE_PASSWORD=your-secure-password
```

## Usage

```bash
# Enable the extension
dream extensions enable flowise

# Start the service
docker compose up -d flowise

# Access at http://localhost:3002
```

## Quick Start

1. **Enable**: `dream extensions enable flowise`
2. **Open**: Visit http://localhost:3002
3. **Create Chatflow**: Click "Add New" → "Chatflow"
4. **Add Nodes**: Drag LLM, memory, and tool nodes
5. **Connect**: Wire nodes together
6. **Test**: Click chat button to test
7. **Deploy**: Export as API or embed

## Example Workflows

### Simple Chatbot
```
Chat Input → OpenAI LLM → Chat Output
```

### RAG Document Chat
```
PDF Loader → Text Splitter → Vector Store → Retriever → OpenAI LLM → Output
```

### AI Agent
```
Chat Input → Agent → [Web Search, Calculator, Code Exec] → LLM → Output
```

## Data Persistence

All flows and data stored in:
- `./data/flowise/` - Workflows, credentials, logs

## Integration with Dream Server

Connect to Dream Server's LLM:
1. Add "ChatLocalAI" or "Ollama" node
2. Set Base URL: `http://llama-server:8080/v1` or `http://ollama:11434`
3. Use models you've downloaded

## Resources

- [Flowise Documentation](https://docs.flowiseai.com/)
- [GitHub Repository](https://github.com/FlowiseAI/Flowise)
- [YouTube Tutorials](https://www.youtube.com/@FlowiseAI)
