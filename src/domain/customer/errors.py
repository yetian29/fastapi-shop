from src.domain.base.errors import BaseDomainException


class CachedDataAreNotFoundException(BaseDomainException):
    pass


class CodesAreNotEqualException(BaseDomainException):
    pass


class CodeIsExpiredException(BaseDomainException):
    pass
