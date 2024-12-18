import os
from dotenv import load_dotenv

# Load the .env file explicitly
load_dotenv(".env.dev")

print("ENV:", os.getenv("ENV"))
print("SQLALCHEMY_DATABASE_URI:", os.getenv("SQLALCHEMY_DATABASE_URI"))
print("BIG_CHAT_API:", os.getenv("BIG_CHAT_API"))
print("OUR_API:", os.getenv("OUR_API"))
