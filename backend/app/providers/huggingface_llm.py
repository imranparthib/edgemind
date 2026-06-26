from app.interfaces.llm import BaseLLM


class HuggingFaceLLMProvider(BaseLLM):

    async def generate(self, message: str) -> str:
        raise NotImplementedError
