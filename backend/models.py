from sqlalchemy import Column, Integer, String
from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Ensure name matches schemas.py
    email = Column(String, unique=True, index=True)
    password = Column(String)
