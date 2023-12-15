import uuid
from pydantic import BaseModel

class IdRead(BaseModel):
    id: uuid.UUID

class ErrorSchema(BaseModel):
    detail: str

class CheckSchema(BaseModel):
    flag: bool
