from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator

from app.models.chat import ChatMessage


class BaseLLM(ABC):

    @abstractmethod
    async def generate(self, messages: list[ChatMessage]) -> str:
        ...

    @abstractmethod
    async def generate_stream(
        self, messages: list[ChatMessage],
    ) -> AsyncGenerator[str, None]:
        ...
