from typing import Final

from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv('.env'))


class Settings(BaseSettings):
    # App settings
    APP_TITLE: Final[str] = 'Litestar Core'
    APP_VERSION: Final[str] = '0.1.0'
    APP_DESCRIPTION: Final[str] = ''

    # Redis settings
    REDIS_CACHE_URL: str = 'redis://localhost:6379/0'

    OPENAPI_URL: str = '/docs'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )


settings = Settings()
