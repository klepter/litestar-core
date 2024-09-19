from typing import Final

from dotenv import load_dotenv, find_dotenv
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv('.env'))


class Settings(BaseSettings):
    # App settings
    APP_TITLE: Final[str] = 'Litestar Core'
    APP_VERSION: Final[str] = '0.1.0'
    APP_DESCRIPTION: Final[str] = ''

    # database settings
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str | int
    DB_USER: str
    DB_PASSWORD: str

    @property
    def DATABASE_URL(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    # Redis settings
    REDIS_CACHE_URL: str = 'redis://localhost:6379/0'

    # openapi config
    OPENAPI_URL: str = '/docs'

    def OPENAPI_CONFIG(self):
        return OpenAPIConfig(
            path=self.OPENAPI_URL,
            title=self.APP_TITLE,
            version=self.APP_VERSION,
            description=self.APP_DESCRIPTION,
            render_plugins=[SwaggerRenderPlugin()],
        )

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )


settings = Settings()
