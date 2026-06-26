from fastapi import FastAPI
from app.api.v1 import health, chat

app = FastAPI(
    title="EdgeMind API",
    description="Intelligent AI Assistant Backend",
    version="0.1.0",
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(chat.router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "message": "Welcome to EdgeMind API 🚀"
    }
