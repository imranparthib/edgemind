import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from app.interfaces.llm import BaseLLM
from app.models.chat import ChatMessage
from app.core.config import settings


class HuggingFaceLLMProvider(BaseLLM):

    def __init__(self) -> None:
        self.model_id = settings.hf_model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = None
        self.model = None

    def load(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_id, use_fast=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto",
        )
        self.model.eval()

    async def generate(self, messages: list[ChatMessage]) -> str:
        if self.tokenizer is None or self.model is None:
            self.load()

        chat = [{"role": m.role, "content": m.content} for m in messages]

        prompt = self.tokenizer.apply_chat_template(
            chat, tokenize=False, add_generation_prompt=True
        )

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.7,
                top_p=0.9,
                do_sample=True,
            )

        decoded = self.tokenizer.decode(
            outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True
        )
        return decoded.strip()
