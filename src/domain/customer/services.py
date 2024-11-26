from abc import ABC, abstractmethod


class ICodeService(ABC):
    @abstractmethod
    def generate_code(
        self, phone_number: str | None = None, email: str | None = None
    ) -> str:
        pass

    @abstractmethod
    def validate_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        pass


class ISendCodeService(ABC):
    @abstractmethod
    def send_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        pass
