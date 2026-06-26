from app.interfaces.llm import BaseLLM


class OllamaLLMProvider(BaseLLM):

    async def generate(self, message: str) -> str:
        raise NotImplementedError
