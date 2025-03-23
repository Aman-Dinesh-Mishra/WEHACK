from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str  
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):  # ✅ Add this missing Token schema
    access_token: str
    token_type: str

class TokenData(BaseModel):  # ✅ Add TokenData for authentication
    email: Optional[str] = None

class LocationCreate(BaseModel):
    latitude: float
    longitude: float

class LocationResponse(BaseModel):
    id: int
    user_id: int
    latitude: float
    longitude: float
    address: Optional[str]  

    class Config:
        from_attributes = True

class EmergencyContactCreate(BaseModel):
    user_id: int
    name: str
    phone: str

class EmergencyContactResponse(BaseModel):
    id: int
    user_id: int
    name: str
    phone: str

    class Config:
        from_attributes = True
