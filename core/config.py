from pydantic import BaseSettings
from pydantic.tools import lru_cache


class AppSettings(BaseSettings):
    debug: bool = True
    app_title: str = "Fastapi Boilerplate."
    app_description: str = "Implementing factory mode for fastapi."
    api_version: str = "v1"
    db_host: str = "127.0.0.1"
    db_port: int = 3306
    db_user: str = "root"
    db_password: str = ""
    db_name: str = "fastapi_boilerplate"
    internal_api_url: str = ""

    class Config:
        env_file = ".env"


@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()


settings = get_app_settings()
