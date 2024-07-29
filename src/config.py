import os

# from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from path import PATH


class Settings(BaseSettings):
    param_name: str
    # token: SecretStr
    ...

    @property
    def fix_param(self):
        """Параметр с фиксированным значением"""
        return

    model_config = SettingsConfigDict(
        env_file=os.path.join(PATH, ".env")
    )


settings = Settings()
