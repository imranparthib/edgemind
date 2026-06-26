from app.interfaces.llm import BaseLLM


class ChatService:

    def __init__(self, llm: BaseLLM) -> None:
        self._llm = llm

    async def chat(self, message: str) -> str:
        return await self._llm.generate(message)
