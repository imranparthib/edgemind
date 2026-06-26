from app.models.chat import ChatMessage

TOKEN_BUDGET = 4096
CHARS_PER_TOKEN = 4


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // CHARS_PER_TOKEN)


def trim_history(
    messages: list[ChatMessage], budget: int = TOKEN_BUDGET,
) -> list[ChatMessage]:
    if not messages:
        return messages

    total = sum(estimate_tokens(m.content) for m in messages)
    if total <= budget:
        return messages

    trimmed = list(messages)
    while trimmed and total > budget:
        for i, m in enumerate(trimmed):
            if m.role != "system":
                total -= estimate_tokens(m.content)
                trimmed.pop(i)
                break
    return trimmed
