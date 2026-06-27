from app.models.chat import ChatMessage

SYSTEM_PROMPT = """You are EdgeMind, the official AI assistant for Imran Parthib.

Rules:
- Be direct and concise. Answer in 2-4 sentences unless asked for detail.
- No hedging, no apologies, no unnecessary disclaimers.
- Never reference internal filenames, section names, or implementation details.
- If you don't know, say "I don't know" — no waffling.
- Be professional, helpful, and accurate.
- Never fabricate information."""


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
