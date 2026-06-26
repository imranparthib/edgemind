from collections.abc import AsyncGenerator

from app.interfaces.memory import BaseMemory
from app.models.chat import ChatMessage
from app.services.context_manager import trim_history
from app.services.llm import LLMService
from app.services.rag import RagService


class ChatService:

    def __init__(
        self,
        llm_service: LLMService,
        rag_service: RagService | None = None,
        memory: BaseMemory | None = None,
    ) -> None:
        self._llm_service = llm_service
        self._rag = rag_service
        self._memory = memory

    def _retrieve_context(self, messages: list[ChatMessage]) -> str | None:
        if self._rag is None:
            return None
        query = messages[-1].content if messages else ""
        chunks = self._rag.retrieve(query)
        if not chunks:
            return None
        return "\n\n".join(chunks)

    async def _build_conversation(
        self, session_id: str, messages: list[ChatMessage],
    ) -> list[ChatMessage]:
        stored = []
        if self._memory:
            stored = await self._memory.get_history(session_id)
        history = [ChatMessage(**m) for m in stored]
        return trim_history(history + messages)

    async def _save_turn(
        self, session_id: str, messages: list[ChatMessage], reply: str,
    ) -> None:
        if self._memory is None:
            return
        for m in messages:
            await self._memory.add(session_id, m.role, m.content)
        await self._memory.add(session_id, "assistant", reply)

    async def chat(
        self, session_id: str, messages: list[ChatMessage],
    ) -> str:
        full = await self._build_conversation(session_id, messages)
        context = self._retrieve_context(full)
        reply = await self._llm_service.generate(full, context=context)
        await self._save_turn(session_id, messages, reply)
        return reply

    async def chat_stream(
        self, session_id: str, messages: list[ChatMessage],
    ) -> AsyncGenerator[str, None]:
        full = await self._build_conversation(session_id, messages)
        context = self._retrieve_context(full)
        reply_chunks: list[str] = []
        async for token in self._llm_service.generate_stream(full, context=context):
            reply_chunks.append(token)
            yield token
        reply = "".join(reply_chunks)
        await self._save_turn(session_id, messages, reply)
