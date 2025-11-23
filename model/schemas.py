from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from enums import enums

class User(BaseModel):
    id: Optional[str] = Field(alias="_id")
    username: str
    email: EmailStr
    password: str
    full_name: str
    role: enums.UserRole
    created_at: datetime
    
    #permiten a pydantic trabajar con tipos personalizados y usar alias en los campos
    class Config:
        populate_byname = True
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str
    role: enums.UserRole

class UserUpdate(BaseModel):
    username: Optional[str] | None = None
    email: Optional[EmailStr] | None = None
    full_name: Optional[str] | None = None
    password: Optional[str] | None = None
    role: Optional[enums.UserRole] | None = None


class TutorAvailability(BaseModel):
    id: Optional[str] = Field(alias="_id")
    tutor_id: str
    day_of_week: enums.WeekDay
    start_time: str
    end_time: str
    
    #permiten a pydantic trabajar con tipos personalizados y usar alias en los campos
    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

class AvailabilityCreate(BaseModel):
    tutor_id: str
    day_of_week: enums.WeekDay
    start_time: str
    end_time: str

class AvailabilityUpdate(BaseModel):
    day_of_week: Optional[enums.WeekDay]
    start_time: Optional[str]
    end_time: Optional[str]


class Class(BaseModel):
    id: Optional[str] = Field(alias="_id")
    tutor_id: str
    student_id: str
    scheduled_date: datetime
    status: str
    notes: Optional[str]

    #permiten a pydantic trabajar con tipos personalizados y usar alias en los campos
    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

class ClassCreate(BaseModel):
    tutor_id: str
    student_id: str
    scheduled_date: datetime
    status: str
    notes: Optional[str]