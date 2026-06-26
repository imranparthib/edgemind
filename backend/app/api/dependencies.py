from app.providers.mock_llm import MockLLMProvider
from app.services.chat_service import ChatService


def get_chat_service() -> ChatService:
    return ChatService(llm=MockLLMProvider())
