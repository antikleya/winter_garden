from fastapi import Response
from fastapi_users.authentication import (
    AuthenticationBackend,
)
from .strategy import DatabaseStrategy
from .models.user import User


class Backend(AuthenticationBackend):
    async def login(self, strategy: DatabaseStrategy, user: User, response: Response):
        access_token = await super().login(strategy, user, response)
        return access_token.__dict__ | {"id": user.id}
