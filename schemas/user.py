from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: int
    email: str
    name: str


class Login(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class Register(BaseModel):
    name: str
    email: str
    password: str


class RegisterResponse(BaseModel):
    name: str
