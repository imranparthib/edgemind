from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

KNOWLEDGE_DIR = Path(__file__).resolve().parent.parent.parent / "knowledge"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


class RagService:

    def __init__(self) -> None:
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.index: faiss.Index | None = None
        self.chunks: list[str] = []

    def ingest(self) -> None:
        chunks: list[str] = []
        for md_path in sorted(KNOWLEDGE_DIR.rglob("*.md")):
            text = md_path.read_text()
            chunks.extend(self._chunk(text, md_path.stem))
        self.chunks = chunks
        if not chunks:
            self.index = None
            return
        embeddings = self.model.encode(chunks, show_progress_bar=False)
        embeddings = np.ascontiguousarray(embeddings, dtype=np.float32)
        faiss.normalize_L2(embeddings)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(embeddings)

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        if self.index is None or not self.chunks:
            return []
        query_vec = self.model.encode([query], show_progress_bar=False)
        query_vec = np.ascontiguousarray(query_vec, dtype=np.float32)
        faiss.normalize_L2(query_vec)
        scores, indices = self.index.search(query_vec, min(top_k, len(self.chunks)))
        return [self.chunks[i] for i in indices[0] if i >= 0]

    def _chunk(self, text: str, source: str) -> list[str]:
        lines = text.strip().split("\n")
        current: list[str] = []
        result: list[str] = []
        for line in lines:
            if line.startswith("## "):
                if current:
                    result.append("\n".join(current))
                current = [line]
            else:
                current.append(line)
        if current:
            result.append("\n".join(current))
        return [f"[{source}] {c.strip()}" for c in result if c.strip()]
