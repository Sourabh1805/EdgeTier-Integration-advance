import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Dynamically select the appropriate .env file
env = os.getenv("ENV", "dev")  # Default to 'dev'
dotenv_file = f"integration/.env.{env}" if env != "dev" else "integration/.env.dev"


# Load the .env file into environment variables
load_dotenv(dotenv_file)


# Define configuration using BaseSettings
class Config(BaseSettings):
    ENV: str
    SQLALCHEMY_DATABASE_URI: str
    BIG_CHAT_API: str
    OUR_API: str

    class Config:
        env_file = (
            dotenv_file  # This tells BaseSettings to load from the specified .env file
        )


# Instantiate settings
# Singleton instance for global use
settings = Config()
