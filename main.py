import uvicorn
from litestar import Litestar
from litestar.config.response_cache import ResponseCacheConfig
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin
from litestar.stores.redis import RedisStore

from src.api import api_router
from src.config.settings import settings

redis_store = RedisStore.with_client(url=settings.REDIS_CACHE_URL, port=6379, db=0)
cache_config = ResponseCacheConfig(store='redis_backed_store')
app = Litestar(
    route_handlers=[api_router],
    stores={'redis_backed_store': redis_store},
    response_cache_config=cache_config,
    openapi_config=OpenAPIConfig(
        path=settings.OPENAPI_URL,
        title=settings.APP_TITLE,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        render_plugins=[SwaggerRenderPlugin()],
    )
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
