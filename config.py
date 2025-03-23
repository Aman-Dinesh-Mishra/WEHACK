import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))  # Default 30 min

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./backend/We_Womensafety.db")  # Default SQLite path

