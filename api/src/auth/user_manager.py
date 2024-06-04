from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin

from .user_database import get_user_db
from .models.user import User

SECRET = "SECRET"


class UserManager(UUIDIDMixin, BaseUserManager[User, str]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    def parse_id(self, value: str) -> str:
        return value


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
