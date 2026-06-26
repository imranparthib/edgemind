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
| Medium | Frontend (Next.js chat UI) |
| Medium | Tool calling (search, browse) |
| Low | Conversation memory expiry / TTL |
| Low | Docker deployment |

## On Hold

| Feature | Reason |
|---|---|
| Milestone 4: Fine-tune in Colab | High risk of regressing instruction-following. Only pursue as a research experiment with a curated dataset. RAG + prompting already cover personalization needs. |
