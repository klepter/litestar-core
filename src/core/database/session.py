from advanced_alchemy.extensions.litestar import AsyncSessionConfig, SQLAlchemyAsyncConfig, SQLAlchemyInitPlugin

from src.config.settings import settings

session_config = AsyncSessionConfig(expire_on_commit=False)
# автоматически создает глобальные зависимости db_session и db_engine,
# названия зависимостей можно поменять через session_dependency_key и engine_dependency_key соответственно
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.DATABASE_URL, session_config=session_config
)
sqlalchemy_plugin = SQLAlchemyInitPlugin(config=sqlalchemy_config)
