from pydantic import EmailStr
from src.core import BaseSchema


class LoginSchema(BaseSchema):
    """
    Schema for user login.

    Attributes:
        email (str): User's email address.
        password (str): User's password.
    """
    email: EmailStr
    password: str


class TokenDataSchema(BaseSchema):
    """
    Schema for token data.

    Attributes:
        user_id (int): The ID of the user associated with the token.
    """
    user_id: int


class TokenSchema(BaseSchema):
    """
    Schema for authentication token.

    Attributes:
        access_token (str): The access token string.
        token_type (str): The type of the token (e.g., "bearer").
    """
    access_token: str
    token_type: str
