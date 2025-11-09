from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core import settings


class DBConnectionHandler:
    """Database connection handler."""

    def __init__(
        self,
        database_url: str = settings.DATABASE_URL,
        echo: bool = settings.DEBUG,
    ):
        self.engine = create_engine(
            database_url,
            echo=echo,
            pool_pre_ping=True,
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
        )
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def get_session(self):
        """Provide a database session."""
        with self.SessionLocal() as session:
            yield session
