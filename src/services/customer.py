from datetime import datetime, timedelta
import random
from typing import Any

from src.domain.customer.errors import (
    CachedDataAreNotFoundException,
    CodeIsExpiredException,
    CodesAreNotEqualException,
)
from src.domain.customer.services import ICodeService, ISendCodeService
from src.helper.errors import fail


class CodeService(ICodeService):
    def __int__(self) -> None:
        self.cache: dict[str, dict[str, Any]] = {}

    def generate_code(
        self, phone_number: str | None = None, email: str | None = None
    ) -> str:
        code = str(random.randin(100000, 999999))
        ttl = timedelta(minutes=1)
        cached_data = {"code": code, "expire_time": datetime.now() + ttl}
        key = phone_number if phone_number else email
        self.cache[key] = cached_data
        return code

    def validate_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        key = phone_number if phone_number else email
        cached_data = self.cache.get(key)
        if not cached_data:
            fail(CachedDataAreNotFoundException)
        elif code != cached_data.get("code"):
            del self.cache[key]
            fail(CodesAreNotEqualException)
        elif datetime.now() > cached_data.get("expire_time"):
            del self.cache[key]
            fail(CodeIsExpiredException)
        del self.cache[key]


class SendCodeService(ISendCodeService):
    def send_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        key = phone_number if phone_number else email
        print(f"The code <{code}> has been sent to phone number or email <{key}>")
