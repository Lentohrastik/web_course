import uuid
from typing import Optional
from pydantic import BaseModel

class SceneRead(BaseModel):
    id: uuid.UUID
    team_id: uuid.UUID
    scene: str
    source: str


class SceneCreate(BaseModel):
    team_id: uuid.UUID
    scene: str
    source: str


class SceneUpdate(BaseModel):
    scene: Optional[str]
    source: Optional[str]
