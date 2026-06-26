from abc import ABC, abstractmethod


class BaseMemory(ABC):

    @abstractmethod
    async def add(self, role: str, content: str) -> None:
        ...

    @abstractmethod
    async def get_history(self) -> list[dict[str, str]]:
        ...
