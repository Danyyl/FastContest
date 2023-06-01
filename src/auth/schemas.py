import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, validator
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    name: str
    score: int


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    name: str
    score: int = 0


class UserUpdate(schemas.BaseUserUpdate):
    pass


class ValidUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=4)
    name: str

    @validator("name")
    def is_name_upper(cls, value):
        if value[0].isupper():
            return value
        else:
            raise ValueError(["Name should be uppercase"])
