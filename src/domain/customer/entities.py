from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Customer:
    oid: UUID | None = None
    phone_number: str = ""
    email: str = ""
    token: UUID | None = None
    is_active: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None
