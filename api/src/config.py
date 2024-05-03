from pydantic import BaseSettings, PostgresDsn
from src.constants import Environment


class Config(BaseSettings):
    DATABASE_URL: PostgresDsn
    DATABASE_URL_ASYNC: PostgresDsn
    DB_POOL_SIZE: int = 50
    DB_MAX_OVERFLOW: int = 50
    ENVIRONMENT: Environment = Environment.PRODUCTION


settings = Config()
