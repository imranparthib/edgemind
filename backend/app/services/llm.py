from app.services.prompt import build_prompt


class LLMService:

    async def generate(self, message: str) -> str:
        prompt = build_prompt(message)

        return (
            "Mock response from EdgeMind.\n\n"
            f"Prompt length: {len(prompt)} characters."
        )


llm_service = LLMService()
