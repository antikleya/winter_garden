from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class HasTimestamp:
    @declared_attr
    def timestamp(cls):
        return Column(
            DateTime(),
            primary_key=True,
        )
