from pathlib import Path

import aiosqlite

from app.interfaces.memory import BaseMemory

DB_PATH = Path(__file__).resolve().parent.parent / "chat_history.db"


class SQLiteHistory(BaseMemory):

    def __init__(self) -> None:
        self._conn: aiosqlite.Connection | None = None

    async def _init_db(self) -> None:
        if self._conn is not None:
            return
        self._conn = await aiosqlite.connect(str(DB_PATH))
        self._conn.row_factory = aiosqlite.Row
        await self._conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await self._conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_history_session
            ON history(session_id)
        """)
        await self._conn.commit()

    async def add(self, session_id: str, role: str, content: str) -> None:
        await self._init_db()
        await self._conn.execute(
            "INSERT INTO history (session_id, role, content) VALUES (?, ?, ?)",
            (session_id, role, content),
        )
        await self._conn.commit()

    async def get_history(self, session_id: str) -> list[dict[str, str]]:
        await self._init_db()
        cursor = await self._conn.execute(
            "SELECT role, content FROM history WHERE session_id = ? ORDER BY id",
            (session_id,),
        )
        rows = await cursor.fetchall()
        return [{"role": row["role"], "content": row["content"]} for row in rows]
