from abc import ABC, abstractmethod

from app.models.chat import ChatMessage


class BaseLLM(ABC):

    @abstractmethod
    async def generate(self, messages: list[ChatMessage]) -> str:
        ...
