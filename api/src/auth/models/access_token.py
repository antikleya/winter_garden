from src.database import Base
from sqlalchemy import Column, ForeignKey, String
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable
from sqlalchemy.orm import declared_attr

from .user import User


class AccessToken(SQLAlchemyBaseAccessTokenTable[str], Base):
    @declared_attr
    def user_id(cls):
        return Column(String(), ForeignKey(User.id, ondelete="cascade"), nullable=False)
