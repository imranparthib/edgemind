# Roadmap

## Completed

| Milestone | Description | Status |
|---|---|---|
| 1 | Replace MockLLMProvider with HuggingFaceLLMProvider (Qwen2.5-1.5B) | ✔ |
| 2 | Streaming token generation via TextIteratorStreamer + SSE | ✔ |
| 3 | RAG with FAISS + Sentence Transformers, knowledge/ ingestion | ✔ |
| — | Conversation memory with SQLite persistence | ✔ |
| — | Structured knowledge base (identity, bio, project, rules) | ✔ |

## Next

| Priority | Feature |
|---|---|
| High | Context control layer (token budget, history trimming) |
| Medium | Conversation memory expiry / TTL |
| Medium | Tool calling (search, browse) |
| Low | Frontend (Next.js chat UI) |
| Low | Docker deployment |
