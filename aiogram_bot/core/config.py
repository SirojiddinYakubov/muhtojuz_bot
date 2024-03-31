import os
import pathlib
from typing import Any
from pydantic import SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = pathlib.Path(__file__).parents[1]
print(8, os.path.join(BASE_DIR, '.env'))


class Settings(BaseSettings):
    TOKEN_API: SecretStr


    # WEBHOOK_HOST: Optional[AnyHttpUrl] = "https://topskill.uz"



    # @field_validator("TOKEN_API", check_fields=False)
    # def assemble_bot_token(cls, v: str, values: dict[str, Any]) -> str:
    #     print(21, cls.BOT_API)
    #     return f"{cls.BOT_API.get_secret_value()}:{cls.BOT_HASH.get_secret_value()}"

    REDIS_HOST: str
    REDIS_PORT: str | int

    ADMIN_IDS: list[int] = [183551051]

    model_config = SettingsConfigDict(
        env_file='.env',
        # env_file=(
        #     os.path.join(BASE_DIR, '.env'),
        #     os.path.join(BASE_DIR, '.env.prod')
        # ),
        env_file_encoding='utf-8',
        # json_encoders={
        #     SecretStr: lambda v: v.get_secret_value() if v else None
        # }
    )


settings = Settings()
