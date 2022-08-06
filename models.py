# Python
from uuid import UUID
from datetime import datetime, date
from typing import Optional
from doctest import Example
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field, validator


class Genders(Enum):
    Male="male"
    Female="female"
    No_binary="no binary"


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(
        ...,
        example="samuraiX@gmail.com"
    )

class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length = 8,
        regex= "(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$",
        description="""Password must be at least 8 characters long, contain at least one 
        uppercase letter, one lowercase letter, one number character."""
        )

class User(BaseModel):

    user_name: str = Field(
        ...,
        min_length=3,
        max_length=25,
        example="samuraiX")
    gender: Optional[Genders] = Field(default=None,example="Male")

    birth_date: date = Field(..., example='1998-06-23')
    def is_over_eighteen(cls, v):
        todays_date = datetime.date.today()
        delta = todays_date - v

        if delta.days/365 <= 18:
            raise ValueError('Must be over 18!')
        else:
            return v

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content:str=Field(
            ...,
            min_length=1,
            max_length=280
    )
    created_at: datetime = Field(default= datetime.now())
    updated_at: Optional[datetime] = Field(default= None)
    by: User = Field(...)