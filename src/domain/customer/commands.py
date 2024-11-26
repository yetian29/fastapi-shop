from dataclasses import dataclass
from src.domain.customer.entities import Customer


@dataclass(frozen=True)
class AuthorizeCustomerCommand:
    customer: Customer


@dataclass(frozen=True)
class LoginCustomerCommand:
    phone_number: str
    email: str
    code: str
