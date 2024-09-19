from litestar import Controller, Router, get


class AccountsController(Controller):
    tags = ['accounts']

    @get(
        description='Just ping',
        cache=300
    )
    async def get_ping(self) -> dict[str, str]:
        return {'ping': 'pong'}


accounts_router = Router(path='/accounts', route_handlers=[AccountsController])
