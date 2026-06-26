from app.interfaces.llm import BaseLLM
from app.models.chat import ChatMessage


class MockLLMProvider(BaseLLM):

    async def generate(self, messages: list[ChatMessage]) -> str:
        last = messages[-1]
        return (
            "Mock response from EdgeMind.\n\n"
            f"You said: {last.content}\n"
            f"Total messages: {len(messages)}"
        )
