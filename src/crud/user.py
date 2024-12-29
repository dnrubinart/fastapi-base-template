from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.user import User


async def read_users(db: AsyncSession):
    """
    Fetch all users from the database.
    """
    result = await db.execute(select(User))
    return result.scalars().all()