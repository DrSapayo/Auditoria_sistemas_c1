from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: Optional[str] = Field(alias="_id")
    username: str
    email: EmailStr
    full_name: str
    role: str
    created_at: datetime
    
    #permiten a pydantic trabajar con tipos personalizados y usar alias en los campos
    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True


class TutorAvailability(BaseModel):
    id: Optional[str] = Field(alias="_id")
    tutor_id: str
    day_of_week: str
    start_time: str
    end_time: str
    
    #permiten a pydantic trabajar con tipos personalizados y usar alias en los campos
    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True


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