from sqlalchemy import Boolean
from sqlalchemy.sql import expression
from sqlalchemy.sql.schema import Column

from fastapi_users.db import SQLAlchemyBaseUserTable

from src.database import Base

from .mixins.has_id import HasId


class User(SQLAlchemyBaseUserTable[str], HasId, Base):
    __tablename__ = "users"
