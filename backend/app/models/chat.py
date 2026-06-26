from typing import Literal

from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    session_id: str = "default"
    messages: list[ChatMessage] = []
    stream: bool = False
