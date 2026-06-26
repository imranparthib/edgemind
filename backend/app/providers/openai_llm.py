from app.interfaces.llm import BaseLLM


class OpenAILLMProvider(BaseLLM):

    async def generate(self, message: str) -> str:
        raise NotImplementedError
