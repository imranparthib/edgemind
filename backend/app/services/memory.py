from collections import defaultdict

from app.interfaces.memory import BaseMemory


class InMemoryHistory(BaseMemory):

    def __init__(self) -> None:
        self._store: dict[str, list[dict[str, str]]] = defaultdict(list)

    async def add(self, session_id: str, role: str, content: str) -> None:
        self._store[session_id].append({"role": role, "content": content})

    async def get_history(self, session_id: str) -> list[dict[str, str]]:
        return list(self._store[session_id])
