# Architecture

## Stack

- **Framework**: FastAPI (Python)
- **LLM**: Qwen2.5-1.5B-Instruct via HuggingFace Transformers
- **Inference**: GPU (NVIDIA GTX 1650 Ti) with float16
- **Vector Store**: FAISS (in-memory, cosine similarity)
- **Embeddings**: all-MiniLM-L6-v2 (Sentence Transformers)
- **Memory**: SQLite via aiosqlite (persistent per-session history)

## Layers

```
Client → FastAPI → ChatService → LLMService → HuggingFaceLLMProvider
                                → RagService  → FAISS index
                                → SQLiteHistory → chat_history.db
```

### API Layer (`api/v1/chat.py`)

Single POST `/chat` endpoint. Accepts `session_id`, `messages`, and `stream` flag. Returns JSON or `StreamingResponse` (SSE).

### Service Layer

| Service | Responsibility |
|---|---|
| `ChatService` | Orchestrator — coordinates memory, RAG, and LLM |
| `LLMService` | Prepends system prompt via `PromptBuilder`, delegates to provider |
| `PromptBuilder` | Builds full message list with system prompt + optional RAG context |
| `RagService` | Ingests knowledge/*.md, chunks by `##` headers, embeds, retrieves top-3 |
| `SQLiteHistory` | Stores per-session conversation history in SQLite |

### Provider Layer

| Provider | Status |
|---|---|
| `HuggingFaceLLMProvider` | Active — local GPU inference with streaming |
| `OpenAILLMProvider` | Stub |
| `OllamaLLMProvider` | Stub |
| `MockLLMProvider` | Removed |

### Interfaces

- `BaseLLM` → `generate()` / `generate_stream()`
- `BaseMemory` → `add()` / `get_history()`

## Data Flow

```
1. POST /chat {session_id, messages, stream}
2. ChatService loads history from SQLiteHistory(session_id)
3. Appends new messages to history
4. RagService.retrieve(last query) → top-3 knowledge chunks
5. PromptBuilder.build(history, context=chunks) → full prompt
6. HuggingFaceLLMProvider.generate(full prompt)
7. ChatService saves assistant reply to SQLiteHistory
8. Return response (JSON or SSE stream)
```

## Knowledge Base

Located at `backend/knowledge/`:

- `identity.md` — EdgeMind's identity and rules
- `imran_parthib.md` — Owner bio, skills, experience
- `edgemind_project.md` — Project description and architecture
- `system_rules.md` — Anti-hallucination and behavior rules
