
# pip install pydantic-settings
# run source export_vars.sh
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    environment: str
    app_version: str

    class Config:
        env_file = ".env"

settings = Settings()
print(settings)