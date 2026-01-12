from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# FORCE load .env from project root
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))


class Settings(BaseSettings):
    APP_NAME: str = "FinSight AI Platform"
    DATABASE_URL: str


settings = Settings()