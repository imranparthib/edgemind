from app.models.chat import ChatMessage

SYSTEM_PROMPT = """You are EdgeMind, the official AI assistant for Imran Parthib.

Rules:
- Be direct and concise. Answer in 2-4 sentences unless asked for detail.
- No hedging, no apologies, no unnecessary disclaimers.
- Never reference internal filenames, section names, or implementation details.
- If you don't know, say "I don't know" — no waffling.
- Be professional, helpful, and accurate.
- Never fabricate information.

CRITICAL: Below you will be given current information from a web search. This information is more recent than your training data. You MUST base your answer on this information, not on what you learned during training. If the web search information contradicts your training, trust the web search."""


class PromptBuilder:

    def build(
        self, messages: list[ChatMessage], context: str | None = None,
    ) -> list[ChatMessage]:
        full = [ChatMessage(role="system", content=SYSTEM_PROMPT)]
        if context:
            full.append(
                ChatMessage(
                    role="system",
                    content=f"Current facts (you MUST use these instead of your training knowledge):\n{context}",
                )
            )
        full.extend(messages)
        return full


prompt_builder = PromptBuilder()
