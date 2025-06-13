from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "changeme"
    DATABASE_URL: str = "sqlite:///./kingstar.db"

    class Config:
        env_file = ".env"
