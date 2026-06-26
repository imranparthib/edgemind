from app.interfaces.llm import BaseLLM
from app.models.chat import ChatMessage
from app.services.prompt import prompt_builder


class LLMService:

    def __init__(self, provider: BaseLLM) -> None:
        self._provider = provider

    async def generate(self, messages: list[ChatMessage]) -> str:
        full = prompt_builder.build(messages)
        return await self._provider.generate(full)
