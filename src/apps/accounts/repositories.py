from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository

from src.apps.accounts.models import User


class UserRepository(SQLAlchemyAsyncRepository[User]):
    model_type = User
