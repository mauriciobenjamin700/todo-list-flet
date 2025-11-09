from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or a .env file.

    Attributes:
        DATABASE_URL (str): The database connection URL.
        SECRET_KEY (str): The secret key for application security.
        DEBUG (bool): Flag to enable or disable debug mode.
    """
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "super_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        str_strip_whitespace=True,
        case_sensitive=True,
        extra="ignore"
    )


settings = Settings()
