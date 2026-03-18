# AnythingLLM Extension

All-in-one AI productivity tool with RAG for Dream Server.

## What It Is

AnythingLLM lets you chat with your documents using AI:
- Upload PDFs, Word docs, text files, code
- Automatic chunking and embedding
- Built-in vector database (LanceDB)
- Multiple LLM provider support
- Fully local, privacy-first

## Features

- **Document chat**: Upload and chat with any document
- **Multi-LLM**: Use Ollama, OpenAI, Anthropic, or local models
- **Built-in embeddings**: Automatic document vectorization
- **Workspaces**: Organize documents into projects
- **Agent support**: Automated workflows and tasks
- **Web browsing**: Optional web search integration
- **Multi-user**: Built-in authentication

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ANYTHINGLLM_PORT` | External port | `3001` |
| `ANYTHINGLLM_JWT_SECRET` | JWT signing secret | (required, 32+ chars) |
| `ANYTHINGLLM_LLM_PROVIDER` | LLM backend | `ollama` |
| `OLLAMA_BASE_PATH` | Ollama API URL | `http://ollama:11434` |
| `OLLAMA_MODEL_PREF` | Default model | `llama3.2` |
| `ANYTHINGLLM_EMBEDDING_ENGINE` | Embedding provider | `ollama` |
| `EMBEDDING_MODEL_PREF` | Embedding model | `nomic-embed-text:latest` |
| `ANYTHINGLLM_VECTOR_DB` | Vector database | `lancedb` |

### LLM Providers

Set `ANYTHINGLLM_LLM_PROVIDER` to one of:
- `ollama` - Local models via Ollama
- `openai` - OpenAI API
- `anthropic` - Claude API
- `azure` - Azure OpenAI
- `localai` - LocalAI endpoint

## Usage

```bash
# Enable the extension
dream extensions enable anythingllm

# Start the service
docker compose up -d anythingllm

# Access at http://localhost:3001
# First run: Create admin account
```

## Setup Steps

1. **Enable**: `dream extensions enable anythingllm`
2. **Start**: `docker compose up -d anythingllm`
3. **Open**: Visit http://localhost:3001
4. **Create workspace**: Click "New Workspace"
5. **Upload documents**: Drag & drop files
6. **Chat**: Ask questions about your documents

## Data Persistence

All data stored in:
- `./data/anythingllm/` - Documents, embeddings, settings

## Integration with Dream Server

By default, uses Dream Server's Ollama extension:
- Set `OLLAMA_BASE_PATH=http://ollama:11434`
- Models auto-detected from Ollama

To use llama-server instead:
1. Set `ANYTHINGLLM_LLM_PROVIDER=openai`
2. Set custom endpoint in UI to `${LLM_API_URL}`

## Security Note

⚠️ **Change the JWT secret before production use:**
```bash
# In your .env
ANYTHINGLLM_JWT_SECRET=your-64-character-random-string-here-please-change-me
```

## Resources

- [AnythingLLM Docs](https://docs.anythingllm.com/)
- [GitHub Repository](https://github.com/Mintplex-Labs/anything-llm)
