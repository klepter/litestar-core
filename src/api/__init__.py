from litestar import Router

from src.api.v1 import v1_router

api_router = Router(path='/api', route_handlers=[v1_router])
