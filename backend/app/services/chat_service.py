from app.services.llm import llm_service


class ChatService:

    async def chat(self, message: str) -> str:
        return await llm_service.generate(message)


chat_service = ChatService()
