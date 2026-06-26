# EdgeMind Project

Description:
EdgeMind is a local AI assistant backend built using FastAPI and HuggingFace Transformers.

Features:
- GPU-based inference (GTX 1650 Ti)
- Streaming responses using TextIteratorStreamer
- Modular LLM provider architecture
- Session-based chat system
- RAG with FAISS and Sentence Transformers (all-MiniLM-L6-v2)

Architecture:
- FastAPI backend
- LLM service abstraction layer
- PromptBuilder for system control
- RagService for retrieval-augmented generation

Current State:
- Milestone 1: Base LLM integration ✔
- Milestone 2: Streaming implemented ✔
- Milestone 3: RAG implemented ✔
