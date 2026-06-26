from app.services.llm import LLMService


class ChatService:

    def __init__(self, llm_service: LLMService | None = None) -> None:
        self._llm_service = llm_service or LLMService()

    async def chat(self, message: str) -> str:
        return await self._llm_service.generate(message)
