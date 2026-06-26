from app.interfaces.llm import BaseLLM
from app.services.prompt import build_prompt


class MockLLMProvider(BaseLLM):

    async def generate(self, message: str) -> str:
        prompt = build_prompt(message)

        return (
            "Mock response from EdgeMind.\n\n"
            f"Prompt length: {len(prompt)} characters."
        )
