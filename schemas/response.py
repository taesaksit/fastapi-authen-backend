from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")


class ResponseSchema(GenericModel, Generic[T]):
    code: int
    status: str
    message: str
    data: Optional[T] = None

    class Config:
        from_attributes = True
