from fastapi_users import FastAPIUsers
from fastapi_users.authentication import BearerTransport
from .strategy import get_auth_strategy
from .user_manager import get_user_manager

from .models.user import User
from .schemas.user import UserRead, UserCreate

from .backend import Backend

auth_backend = Backend(
    name="jwt",
    transport=BearerTransport(tokenUrl="/login"),
    get_strategy=get_auth_strategy,
)
fastapi_users = FastAPIUsers[User, str](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True, verified=True)
optional_user = fastapi_users.current_user(optional=True, active=True, verified=True)

login_router = fastapi_users.get_auth_router(auth_backend)
registration_router = fastapi_users.get_register_router(UserRead, UserCreate)
