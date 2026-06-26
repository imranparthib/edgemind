from abc import ABC, abstractmethod


class BaseVectorStore(ABC):

    @abstractmethod
    async def search(self, query: str, top_k: int = 5) -> list[dict]:
        ...
