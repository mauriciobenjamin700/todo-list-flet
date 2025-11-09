from datetime import datetime, timedelta
from typing import Any

from bcrypt import hashpw, gensalt, checkpw
from jose import JWTError, jwt

from src.core import settings


class PasswordHasher:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a plaintext password using bcrypt.

        Args:
            password (str): The plaintext password to hash.

        Returns:
            str: The hashed password.
        """
        hashed = hashpw(password.encode('utf-8'), gensalt())
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a plaintext password against a hashed password.

        Args:
            plain_password (str): The plaintext password to verify.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )


class TokenHandler:
    """
    Utility class for creating and verifying JWT tokens.

    Methods:
        - create_access_token
        - verify_token
    """
    @staticmethod
    def create_access_token(
        data: dict[str, Any],
        secret_key: str = settings.SECRET_KEY,
        algorithm: str = settings.ALGORITHM,
        expires_delta: timedelta | None = None
    ) -> str:
        """Create a JWT access token.

        Args:
            data (dict): The data to encode in the token.
            secret_key (str): The secret key to sign the token.
            algorithm (str): The signing algorithm.
            expires_delta (timedelta | None): Optional expiration time for
            the token.

        Returns:
            str: The encoded JWT token.
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
        return encoded_jwt

    @staticmethod
    def verify_token(
        token: str,
        secret_key: str = settings.SECRET_KEY,
        algorithms: list[str] = [settings.ALGORITHM]
    ) -> dict[str, Any]:
        """Verify a JWT token and decode its payload.

        Args:
            token (str): The JWT token to verify.
            secret_key (str): The secret key used to sign the token.
            algorithms (list[str]): List of acceptable signing algorithms.
        Returns:
            dict: The decoded token payload.
        Raises:
            JWTError: If the token is invalid or expired.
        """
        try:
            payload = jwt.decode(token, secret_key, algorithms=algorithms)
            return payload
        except JWTError:
            raise JWTError("Token verification failed")
