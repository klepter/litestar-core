from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.accounts.repositories import UserRepository


async def provide_user_repository(db_session: AsyncSession) -> UserRepository:
    return UserRepository(session=db_session)
