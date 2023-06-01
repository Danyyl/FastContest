import uuid
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field, validator

from auth.schemas import UserRead
from tasks.utils import StatusEnum


# Topic schemas
class TopicScheme(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class TopicCreate(BaseModel):
    name: str


class TopicUpdate(BaseModel):
    id: int
    name: str


# Tag schemas
class TagScheme(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class TagCreate(BaseModel):
    name: str


# TaskTag schemas
class TaskTagScheme(BaseModel):
    id: int
    tag: TagScheme

    class Config:
        orm_mode = True


class TaskTagCreate(BaseModel):
    task_id: int
    tag_id: int


# Task schemas
class TaskScheme(BaseModel):
    id: int
    name: str
    text: str
    topic: Optional[TopicScheme]
    score: int
    tags: Optional[List[TaskTagScheme]]

    class Config:
        orm_mode = True


class SimpleTaskScheme(BaseModel):
    id: int
    name: str
    text: str

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    name: str
    text: str
    topic_id: int
    score: Optional[int] = 0


class TaskUpdate(BaseModel):
    id: int
    name: Optional[str]
    text: Optional[str]
    topic: Optional[int]
    score: Optional[int]


# UserTask schemas
class UserTaskScheme(BaseModel):
    id: int
    task: SimpleTaskScheme
    answer: Optional[str]
    status: StatusEnum
    score: int
    submitted: bool
    submitted_at: datetime

    class Config:
        orm_mode = True


class UserTaskCreate(BaseModel):
    task_id: int
    user_id: int


class UserTaskUpdate(BaseModel):
    answer: Optional[str]

    @validator("answer")
    def is_correct_func(cls, value=None):
        if all([temp in value for temp in ["return", "def"]]) or not value:
            return value
        else:
            raise ValueError(["Wrong method format, no return or def statement"])


# class ValidUser(BaseModel):
#     email: EmailStr
#     password: str = Field(min_length=4)
#     name: str
#
#     @validator("name")
#     def is_name_upper(cls, value):
#         if value[0].isupper():
#             return value
#         else:
#             raise ValueError(["Name should be uppercase"])
