from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core import BaseModel, tables


class UserModel(BaseModel):
    """
    User model representing a user in the system.

    Attributes:
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The hashed password of the user.
        id (int): The unique identifier of the user.
        created_at (datetime): The timestamp when the user was created.
        updated_at (datetime): The timestamp when the user was last updated.
    """
    __tablename__ = tables.USER_TABLE_NAME

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True
    )
    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
