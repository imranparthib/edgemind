import asyncio
from concurrent.futures import ThreadPoolExecutor

from ddgs import DDGS

_executor = ThreadPoolExecutor(max_workers=1)


class WebSearchService:

    def __init__(self, enabled: bool = True) -> None:
        self._enabled = enabled

    async def search(self, query: str, max_results: int = 3) -> list[str]:
        if not self._enabled or not query:
            return []
        current_year = "2026"
        time_words = {"current", "latest", "recent", "now", "today", "new", "update"}
        if any(w in query.lower() for w in time_words):
            query = f"{query} {current_year}"
        loop = asyncio.get_running_loop()
        results: list[dict] = await loop.run_in_executor(
            _executor, self._search_sync, query, max_results,
        )
        seen: set[str] = set()
        out: list[str] = []
        for r in results:
            body = (r.get("body") or "").strip()
            if body and body not in seen:
                seen.add(body)
                out.append(f"• {body}")
        return out

    def _search_sync(self, query: str, max_results: int) -> list[dict]:
        try:
            with DDGS() as ddgs:
                return list(ddgs.text(query, max_results=max_results))
        except Exception:
            return []
