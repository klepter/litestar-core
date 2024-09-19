from litestar import Controller, Router, get
from litestar.di import Provide
from litestar.pagination import OffsetPagination
from litestar.repository.filters import LimitOffset
from pydantic import TypeAdapter

from src.apps.accounts.dependencies import provide_user_repository
from src.apps.accounts.models import User
from src.apps.accounts.repositories import UserRepository


class AccountsController(Controller):
    tags = ['accounts']
    dependencies = {'user_repository': Provide(provide_user_repository)}

    @get(
        path='/ping',
        description='Just ping',
        cache=300
    )
    async def get_ping(self) -> dict[str, str]:
        return {'ping': 'pong'}

    @get(
        path='/users',
        description='Get users',
        cache=300
    )
    async def get_users(
        self,
        user_repository: UserRepository,
        limit_offset: LimitOffset
    ) -> OffsetPagination[User]:
        results, total = await user_repository.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[User])
        return OffsetPagination[User](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset
        )


accounts_router = Router(path='/accounts', route_handlers=[AccountsController])
