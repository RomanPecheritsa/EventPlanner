from pydantic import BaseModel, EmailStr, Extra
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }

