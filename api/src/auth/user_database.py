from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from src.database import get_async_session
from .models.user import User


class UserDatabase(SQLAlchemyUserDatabase):
    def __init__(self, session: AsyncSession):
        super().__init__(session, User, None)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield UserDatabase(session)
