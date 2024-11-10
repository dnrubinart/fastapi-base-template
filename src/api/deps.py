from typing import Generator

from repositories.db_session import SessionLocal


def get_db() -> Generator:
    """
    Get a database connection from the connection pool and return it to the pool when the request is finished.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
