from app.models.chat import ChatMessage
from app.services.llm import LLMService


class ChatService:

    def __init__(self, llm_service: LLMService) -> None:
        self._llm_service = llm_service

    async def chat(self, messages: list[ChatMessage]) -> str:
        return await self._llm_service.generate(messages)
