from litestar import Router

from src.api.v1.accounts.controllers import accounts_router

v1_router = Router(path='/v1', route_handlers=[
    accounts_router
])
