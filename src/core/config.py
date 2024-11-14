import logging

# from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from core.path import PATH

logger = logging.getLogger()


class Settings(BaseSettings):
    PARAM: str
    # TOKEN: SecretStr
    ...

    @property
    def fix_param(self):
        """Параметр с фиксированным значением"""
        return

    model_config = SettingsConfigDict(
        env_file=PATH / ".env", env_file_encoding="utf-8", extra="ignore"
    )


try:
    settings = Settings()

except ValueError:
    logger.exception("Ошибка загрузки входных параметров")
    raise
