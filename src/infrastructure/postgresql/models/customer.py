from datetime import datetime
from uuid import UUID, uuid4
from src.infrastructure.postgresql.models.base import BaseORM
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func


class CustomerORM(BaseORM):
    __tablename__ = "customer"

    oid: Mapped[UUID] = mapped_column(
        default=uuid4, primary_key=True, nullable=False, unique=True
    )
    phone_number: Mapped[str] = mapped_column(default="")
    email: Mapped[str] = mapped_column(default="")
    token: Mapped[UUID] = mapped_column(default=None, nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now())
