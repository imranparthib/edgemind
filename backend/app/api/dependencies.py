from app.providers.mock_llm import MockLLMProvider
from app.services.chat_service import ChatService
from app.services.llm import LLMService


def get_chat_service() -> ChatService:
    return ChatService(llm_service=LLMService(provider=MockLLMProvider()))
