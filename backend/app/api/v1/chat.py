from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.models.response import ChatResponse
from app.services.chat_service import chat_service

router = APIRouter(tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = await chat_service.chat(request.message)
    return ChatResponse(reply=reply)
