from collections.abc import AsyncGenerator

from app.interfaces.llm import BaseLLM
from app.models.chat import ChatMessage
from app.services.prompt import prompt_builder


class LLMService:

    def __init__(self, provider: BaseLLM) -> None:
        self._provider = provider

    async def generate(
        self, messages: list[ChatMessage], context: str | None = None,
    ) -> str:
        full = prompt_builder.build(messages, context=context)
        return await self._provider.generate(full)

    async def generate_stream(
        self, messages: list[ChatMessage], context: str | None = None,
    ) -> AsyncGenerator[str, None]:
        full = prompt_builder.build(messages, context=context)
        async for token in self._provider.generate_stream(full):
            yield token
