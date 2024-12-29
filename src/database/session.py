from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.core.config import settings
from models.base import Base

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


async def init_db():
    """
    Create all tables in the database.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
