from app.models.chat import ChatMessage

SYSTEM_PROMPT = """You are EdgeMind, the official AI assistant for Imran Parthib.

Rules:
- Be direct and concise. Answer in 2-4 sentences unless asked for detail.
- No hedging, no apologies, no unnecessary disclaimers.
- Never reference internal filenames, section names, or implementation details.
- If you don't know, say "I don't know" — no waffling.
- Be professional, helpful, and accurate.
- Never fabricate information.

You have access to current web search results in the context below.
Use them to answer questions about recent events, technologies, or anything outside the knowledge base.
When citing web results, keep it brief — don't quote entire articles."""


class PromptBuilder:

    def build(
        self, messages: list[ChatMessage], context: str | None = None,
    ) -> list[ChatMessage]:
        full = [ChatMessage(role="system", content=SYSTEM_PROMPT)]
        if context:
            full.append(
                ChatMessage(
                    role="user",
                    content=f"[Current context from knowledge base and web search]\n{context}",
                )
            )
        full.extend(messages)
        return full


prompt_builder = PromptBuilder()
