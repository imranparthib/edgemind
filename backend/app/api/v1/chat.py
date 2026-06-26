from fastapi import APIRouter, Depends

from app.api.dependencies import get_chat_service
from app.models.chat import ChatRequest
from app.models.response import ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service),
):
    reply = await service.chat(request.messages)
    return ChatResponse(session_id=request.session_id, reply=reply)
