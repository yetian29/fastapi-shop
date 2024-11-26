from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.exc import SQLAlchemyError


class DatabaseManager:
    def __init__(self, url: str) -> None:
        self._async_engine = create_async_engine(
            url=url, echo=True, isolation_level="READ COMMITED"
        )
        """expire_on_commit: don't expire objects after  transaction commit"""
        self._async_session = async_sessionmaker(
            bind=self._async_engine, expire_on_commit=False
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, Any]:
        session: AsyncSession = self._async_session
        try:
            yield session
        except SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.commit()
            await session.close()
