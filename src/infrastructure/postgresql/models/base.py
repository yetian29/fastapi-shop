from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class BaseORM(AsyncAttrs, DeclarativeBase):
    pass
