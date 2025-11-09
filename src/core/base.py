from datetime import datetime

from pydantic import BaseModel, ConfigDict
from sqlalchemy import Integer, TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseSchema(BaseModel):
    """
    Base schema for Pydantic models with common configuration.
    """
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        use_enum_values=True,
        extra="ignore"
    )


class BaseModel(DeclarativeBase):
    """
    Base class for SQLAlchemy ORM models.

    Includes common fields for all database tables.

    Attributes:
        id (int): Primary key identifier.
        created_at (datetime): Timestamp of record creation.
        updated_at (datetime): Timestamp of last record update.
    """
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )


class BaseDBSchema(BaseSchema):
    """
    Base schema for database entities, extending BaseSchema.

    Attributes:
        id (int): Primary key identifier.
        created_at (datetime): Timestamp of record creation.
        updated_at (datetime): Timestamp of last record update.
    """
    id: int
    created_at: datetime
    updated_at: datetime
