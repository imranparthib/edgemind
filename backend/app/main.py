from fastapi import FastAPI

app = FastAPI(
    title="EdgeMind API",
    description="Intelligent AI Assistant Backend",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to EdgeMind API 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }