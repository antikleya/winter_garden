from sqlalchemy import Column, String
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import declarative_mixin
from src.utils import generate_shortid


@declarative_mixin
class HasId:
    @declared_attr
    def id(cls):
        return Column(
            String(),
            primary_key=True,
            default=generate_shortid
        )
