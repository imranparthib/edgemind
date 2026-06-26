from abc import ABC, abstractmethod


class BaseMemory(ABC):

    @abstractmethod
    async def add(self, session_id: str, role: str, content: str) -> None:
        ...

    @abstractmethod
    async def get_history(self, session_id: str) -> list[dict[str, str]]:
        ...
