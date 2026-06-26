from app.core.config import settings
from app.providers.huggingface_llm import HuggingFaceLLMProvider
from app.services.chat_service import ChatService
from app.services.llm import LLMService


def get_chat_service() -> ChatService:
    provider = HuggingFaceLLMProvider()
    provider.load()
    return ChatService(llm_service=LLMService(provider=provider))
