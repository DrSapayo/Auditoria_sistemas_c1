from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: float = Field(ge=0)

class BookOut(BookCreate):
    id: str

class UserCrate(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserOut(BaseModel):
    id: str
    email: EmailStr
    name: str
    role: str = "user"

class PurchaseCreate(BaseModel):
    book_id:str
    quantity: int = Field(ge=1)

class PurchaseOut(BaseModel):
    id:str
    user_id: str
    book_id: str
    quantity: int
    purchased_at: datetime