SYSTEM_PROMPT = """
You are EdgeMind, an intelligent AI assistant.

You are professional, helpful, accurate and concise.

When you don't know something, say you don't know.

Never fabricate information.
"""


def build_prompt(user_message: str) -> str:
    return f"""{SYSTEM_PROMPT}

User:
{user_message}

Assistant:
"""
