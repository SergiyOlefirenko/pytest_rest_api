from pydantic import BaseModel, validator, EmailStr
from src.enums.user_enums import Genders, Statuses


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    gender: Genders
    status: Statuses
