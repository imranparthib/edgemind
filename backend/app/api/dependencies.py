from app.core.config import settings
from app.interfaces.llm import BaseLLM
from app.providers.hf_api import HuggingFaceInferenceAPIProvider
from app.providers.huggingface_llm import HuggingFaceLLMProvider
from app.services.chat_service import ChatService
from app.services.llm import LLMService
from app.services.memory import SQLiteHistory
from app.services.rag import RagService


_provider: BaseLLM | None = None
_rag_service: RagService | None = None
_memory: SQLiteHistory | None = None


def _create_provider() -> BaseLLM:
    if settings.llm_provider == "hf_api":
        return HuggingFaceInferenceAPIProvider()
    return HuggingFaceLLMProvider()


def get_chat_service() -> ChatService:
    global _provider, _rag_service, _memory
    if _provider is None:
        _provider = _create_provider()
        if isinstance(_provider, HuggingFaceLLMProvider):
            _provider.load()
    if _rag_service is None:
        _rag_service = RagService()
        _rag_service.ingest()
    if _memory is None:
        _memory = SQLiteHistory()
    return ChatService(
        llm_service=LLMService(provider=_provider),
        rag_service=_rag_service,
        memory=_memory,
    )
