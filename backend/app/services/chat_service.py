from collections.abc import AsyncGenerator

from app.models.chat import ChatMessage
from app.services.llm import LLMService
from app.services.rag import RagService


class ChatService:

    def __init__(
        self, llm_service: LLMService, rag_service: RagService | None = None,
    ) -> None:
        self._llm_service = llm_service
        self._rag = rag_service

    def _retrieve_context(self, messages: list[ChatMessage]) -> str | None:
        if self._rag is None:
            return None
        query = messages[-1].content if messages else ""
        chunks = self._rag.retrieve(query)
        if not chunks:
            return None
        return "\n\n".join(chunks)

    async def chat(self, messages: list[ChatMessage]) -> str:
        context = self._retrieve_context(messages)
        return await self._llm_service.generate(messages, context=context)

    async def chat_stream(
        self, messages: list[ChatMessage],
    ) -> AsyncGenerator[str, None]:
        context = self._retrieve_context(messages)
        async for token in self._llm_service.generate_stream(messages, context=context):
            yield token
