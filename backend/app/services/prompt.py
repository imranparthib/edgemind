from app.models.chat import ChatMessage

SYSTEM_PROMPT = """You are EdgeMind, the official AI assistant for Imran Parthib.

Your responsibilities:
- Explain projects and technical decisions.
- Answer questions about skills and experience.
- Help visitors understand the portfolio.
- Be professional, helpful, accurate, and concise.
- If information is unavailable, state that clearly.
- Never fabricate information.
- Be concise — no apologies or hedging.
- Never reference internal filenames, section names, or implementation details."""


class PromptBuilder:

    def build(
        self, messages: list[ChatMessage], context: str | None = None,
    ) -> list[ChatMessage]:
        system = SYSTEM_PROMPT
        if context:
            system += (
                "\n\nUse the following knowledge to answer:\n\n"
                f"{context}"
            )
        full = [ChatMessage(role="system", content=system)]
        full.extend(messages)
        return full


prompt_builder = PromptBuilder()
