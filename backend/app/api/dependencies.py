from app.core.config import settings
from app.providers.huggingface_llm import HuggingFaceLLMProvider
from app.services.chat_service import ChatService
from app.services.llm import LLMService
from app.services.rag import RagService


_provider: HuggingFaceLLMProvider | None = None
_rag_service: RagService | None = None


def get_chat_service() -> ChatService:
    global _provider, _rag_service
    if _provider is None:
        _provider = HuggingFaceLLMProvider()
        _provider.load()
    if _rag_service is None:
        _rag_service = RagService()
        _rag_service.ingest()
    return ChatService(llm_service=LLMService(provider=_provider), rag_service=_rag_service)
