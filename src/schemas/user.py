from pydantic import EmailStr

from src.core import BaseSchema, BaseDBSchema


class UserCreateSchema(BaseSchema):
    """
    Schema for creating a new user.

    Attributes:
        name (str): The name of the user.
        email (EmailStr): The email address of the user.
        password (str): The password for the user.
    """
    name: str
    email: EmailStr
    password: str


class UserUpdateSchema(BaseSchema):
    """
    Schema for updating an existing user.

    Attributes:
        name (str | None): The updated name of the user.
        email (EmailStr | None): The updated email address of the user.
        password (str | None): The updated password for the user.
    """
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class UserDBSchema(BaseDBSchema):
    """
    Schema representing a user in the database.

    Attributes:
        name (str): The name of the user.
        email (EmailStr): The email address of the user.
        password (str): The password for the user.
        id (int): Primary key identifier.
        created_at (datetime): Timestamp of record creation.
        updated_at (datetime): Timestamp of last record update.
    """
    name: str
    email: EmailStr
    password: str


class UserResponseSchema(UserDBSchema):
    """
    Schema for user data returned in responses.

    Attributes:
        name (str): The name of the user.
        email (EmailStr): The email address of the user.
        id (int): Primary key identifier.
        created_at (datetime): Timestamp of record creation.
        updated_at (datetime): Timestamp of last record update.
    """
    name: str
    email: EmailStr
