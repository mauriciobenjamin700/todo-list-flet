from datetime import datetime

from pydantic import BaseModel, ConfigDict
from sqlalchemy import Integer, TIMESTAMP, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from typing import TypeVar, Generic, Type


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


T = TypeVar("T", bound=BaseModel)


class BaseRepository(Generic[T]):
    """
    Base repository class for database operations.

    Attributes:
        session (Session): SQLAlchemy session for database interactions.
        model (Type[T]): The ORM model class associated with this repository.

    Methods:
        - add
        - get
        - list
        - update
        - delete
    """
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model: Type[T] = model

    def add(self, instance: T) -> T:
        """
        Add a new instance to the database.

        Args:
            instance (BaseModel): The instance to add.

        Returns:
            BaseModel: The added instance.
        """
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get(self, instance_id: int) -> T | None:
        """
        Retrieve an instance by its ID.

        Args:
            instance_id (int): The ID of the instance to retrieve.

        Returns:
            BaseModel | None: The retrieved instance or None if not found.
        """
        stmt = select(self.model).where(self.model.id == instance_id)
        result = self.session.execute(stmt).scalar_one_or_none()
        return result

    def list(self) -> list[T]:
        """
        Retrieve all instances of the model.

        Returns:
            list[BaseModel]: A list of all instances.
        """
        stmt = select(self.model)
        result = self.session.execute(stmt).scalars().all()
        return result

    def update(self, instance: T) -> T:
        """
        Update an existing instance in the database.

        Args:
            instance (BaseModel): The instance to update.

        Returns:
            BaseModel: The updated instance.
        """
        self.session.merge(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, instance: T) -> None:
        """
        Delete an instance from the database.

        Args:
            instance (BaseModel): The instance to delete.
        """
        self.session.delete(instance)
        self.session.commit()
