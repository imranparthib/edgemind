from app.interfaces.llm import BaseLLM


class LLMService:

    def __init__(self, provider: BaseLLM) -> None:
        self._provider = provider

    async def generate(self, message: str) -> str:
        return await self._provider.generate(message)
