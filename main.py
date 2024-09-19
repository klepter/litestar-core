import uvicorn
from litestar import Litestar
from litestar.config.response_cache import ResponseCacheConfig
from litestar.stores.redis import RedisStore

from src.api import api_router
from src.config.settings import settings
from src.core.database.session import sqlalchemy_plugin
from src.core.dependencies.app_deps import app_dependencies as dependencies

redis_store = RedisStore.with_client(url=settings.REDIS_CACHE_URL, port=6379, db=0)
cache_config = ResponseCacheConfig(store='redis_backed_store')

app = Litestar(
    route_handlers=[api_router],
    stores={'redis_backed_store': redis_store},
    response_cache_config=cache_config,
    openapi_config=settings.OPENAPI_CONFIG(),
    plugins=[sqlalchemy_plugin],
    dependencies=dependencies
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
