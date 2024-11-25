from src.core.config import settings
from sqlalchemy.ext.asyncio import AsyncEngine


class _DatabaseManager:
    _user: str
    _password: str
    _host: str
    _port: str
    _db: str
    _engine: AsyncEngine | None = None

    def __init__(self):
        user = settings.Database.POSTGRES_USER
        password = settings.Database.POSTGRES_PASSWORD
        host = settings.Database.POSTGRES_HOST
        port = settings.Database.POSTGRES_PORT
        db = settings.Database.POSTGRES_DB

        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._db = db


class DatabaseManagerAsync(_DatabaseManager):
    pass
