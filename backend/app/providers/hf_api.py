import json
from collections.abc import AsyncGenerator

import httpx

from app.core.config import settings
from app.interfaces.llm import BaseLLM
from app.models.chat import ChatMessage

HF_API_BASE = "https://api-inference.huggingface.co/v1"


class HuggingFaceInferenceAPIProvider(BaseLLM):

    def __init__(self) -> None:
        self.model_id = settings.hf_model
        self.headers = {
            "Authorization": f"Bearer {settings.hf_token}",
            "Content-Type": "application/json",
        }

    def _build_payload(
        self, messages: list[ChatMessage], stream: bool = False,
    ) -> dict:
        return {
            "model": self.model_id,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "max_tokens": 256,
            "temperature": 0.7,
            "top_p": 0.9,
            "stream": stream,
        }

    async def generate(self, messages: list[ChatMessage]) -> str:
        payload = self._build_payload(messages)
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{HF_API_BASE}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=60,
            )
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]

    async def generate_stream(
        self, messages: list[ChatMessage],
    ) -> AsyncGenerator[str, None]:
        payload = self._build_payload(messages, stream=True)
        async with httpx.AsyncClient() as client:
            async with client.stream(
                "POST",
                f"{HF_API_BASE}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=120,
            ) as resp:
                resp.raise_for_status()
                async for line in resp.aiter_lines():
                    if not line.startswith("data: "):
                        continue
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        delta = chunk["choices"][0].get("delta", {})
                        token = delta.get("content", "")
                        if token:
                            yield token
                    except json.JSONDecodeError:
                        continue
