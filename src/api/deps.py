from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.session import SessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Get a database connection from the connection pool and return it
    to the pool when the request is finished.
    """
    async with SessionLocal() as db:
        yield db