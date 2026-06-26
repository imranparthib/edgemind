# EdgeMind

EdgeMind is an intelligent AI assistant designed to understand and interact with a personalized knowledge base using modern LLM technologies.

## Features

- FastAPI backend
- Fine-tuned Hugging Face models
- Retrieval-Augmented Generation (RAG)
- Conversation memory
- Semantic search
- REST API
- Portfolio knowledge base
- Tool calling (planned)

## Tech Stack

- Python
- FastAPI
- Transformers
- PyTorch
- PEFT (LoRA)
- Qdrant
- Sentence Transformers
- Docker

## Project Status

🚧 Under active development.


Notes:

My proposal

I think we're entering Sprint 2, and I'd like us to do it in four milestones:

Milestone 1 (Today)
Replace MockLLMProvider with a real HuggingFaceLLMProvider.
Verify that EdgeMind can generate responses locally.
Milestone 2
Add streaming token generation so your portfolio can display responses as they're generated.
Milestone 3
Add RAG, connecting the knowledge/ directory so EdgeMind answers using your portfolio content instead of relying only on the model's general knowledge.
Milestone 4
Fine-tune the model in Google Colab, upload it to Hugging Face, and then change only the MODEL_ID in your configuration to switch from the base model to your own EdgeMind model.