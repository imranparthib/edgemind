from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import chat_service

router = APIRouter(tags=["Chat"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = await chat_service.chat(request.message)
    return ChatResponse(reply=reply)
