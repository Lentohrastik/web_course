from typing import List, Optional
import uuid
from pydantic import BaseModel

class PhotoRead(BaseModel):
    id: uuid.UUID
    name: str
    role: str
    embeding: List[float]
    team_id: uuid.UUID
    url: str


class PhotoCreate(BaseModel):
    name: str
    role: str
    embeding: List[float]
    team_id: uuid.UUID
    url: str


class PhotoUpdate(BaseModel):
    name: Optional[str]
    role: Optional[str]
    embeding: Optional[List[float]]
    team_id: Optional[uuid.UUID]
    url: Optional[str]