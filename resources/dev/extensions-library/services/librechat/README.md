# LibreChat Extension

Enhanced ChatGPT clone with multi-provider AI support for Dream Server.

## What It Is

LibreChat provides a polished chat interface supporting multiple LLM providers:
- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)
- Google (Gemini)
- Azure OpenAI
- Groq
- Mistral
- OpenRouter
- Custom OpenAI-compatible endpoints

## Features

- **Multi-provider chat**: Switch between AI providers in one conversation
- **RAG support**: Upload documents for AI to reference
- **AI agents**: Plugin and tool support
- **File uploads**: Images, documents, code files
- **Conversation history**: Persistent chat history
- **Multi-user**: Built-in authentication system
- **Search**: Full-text search across conversations

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `LIBRECHAT_PORT` | External port | `3080` |
| `LIBRECHAT_MONGO_PASSWORD` | MongoDB root password | `librechat123` |
| `LIBRECHAT_MEILI_KEY` | Meilisearch master key | `librechat_meili_master_key` |

### API Keys (Optional)

Set any of these to enable the corresponding provider:
- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_KEY`
- `AZURE_OPENAI_API_KEY`
- `GROQ_API_KEY`
- `MISTRAL_API_KEY`
- `OPENROUTER_KEY`
- `DEEPSEEK_API_KEY`

## Usage

```bash
# Enable the extension
dream extensions enable librechat

# Start the services
docker compose up -d librechat

# Access at http://localhost:3080
```

## Data Persistence

User data is stored in:
- `./data/librechat/mongodb/` - Chat history and user data
- `./data/librechat/meilisearch/` - Search index
- `./data/librechat/images/` - Uploaded images
- `./data/librechat/uploads/` - File uploads
- `./data/librechat/logs/` - Application logs

## Integration with Dream Server

LibreChat can use Dream Server's llama-server as a custom endpoint:
1. Go to Settings → Endpoints
2. Add custom endpoint: `http://llama-server:8080/v1`
3. Set API key to any value (local llama-server doesn't require auth)

## Resources

- [LibreChat Documentation](https://www.librechat.ai/docs)
- [GitHub Repository](https://github.com/danny-avila/LibreChat)
