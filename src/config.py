import logging

# from pydantic import SecretStr
from pydantic_settings import BaseSettings


class ExtraFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        self._style._fmt = self._fmt

        default_attrs = logging.LogRecord(*[None] * 7).__dict__.keys()
        extras = set(record.__dict__.keys()) - default_attrs - {"message"}
        if extras:
            format_str = "\n" + "\n".join(f"{val}: %({val})s" for val in sorted(extras))
            self._style._fmt += format_str

        return super().format(record)


class Settings(BaseSettings):
    param_name: str
    # token: SecretStr
    ...

    @property
    def fix_param(self):
        """Параметр с фиксированным значением"""
        return


settings = Settings()
