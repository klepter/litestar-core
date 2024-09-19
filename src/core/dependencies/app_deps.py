from litestar.di import Provide

from src.core.dependencies.limit_offset import provide_limit_offset_pagination

app_dependencies: dict[str, any] = {
    'limit_offset': Provide(provide_limit_offset_pagination)
}
