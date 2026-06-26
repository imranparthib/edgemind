from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["Chat"])


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):
    return {
        "reply": f"You said: {request.message}"
    }
