from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "EdgeMind"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    hf_model: str = "Qwen/Qwen2.5-1.5B-Instruct"
    hf_token: str = ""

    qdrant_url: str = "http://localhost:6333"

    database_url: str = ""


settings = Settings()
