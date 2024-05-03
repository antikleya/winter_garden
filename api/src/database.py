import logging
from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from src.config import settings
from src.constants import Environment

DATABASE_URL = settings.DATABASE_URL

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, echo=False, future=True, echo_pool=True,
                       pool_size=settings.DB_POOL_SIZE, max_overflow=settings.DB_MAX_OVERFLOW, pool_pre_ping=True)
session_maker = sessionmaker(bind=engine)

async_engine = create_async_engine(settings.DATABASE_URL_ASYNC)
async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


def get_session():
    session: Session = session_maker()
    if settings.ENVIRONMENT == Environment.LOCAL:
        yield session
    else:
        try:
            yield session
        except Exception as e:
            session.rollback()
            logging.error(e)
        finally:
            session.close()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
