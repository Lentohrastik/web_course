import uuid
from typing import Optional
from pydantic import BaseModel


class TeamRead(BaseModel):
    id: uuid.UUID
    name: str
    template_id: int
    owner: uuid.UUID

    obs_host: str
    obs_port: int
    obs_password: str


class TeamCreate(BaseModel):
    name: str
    password: str
    owner: uuid.UUID
    template_id: Optional[int]

    obs_host: Optional[str]
    obs_port: Optional[int]
    obs_password: Optional[str]


class TeamUpdate(BaseModel):
    name: Optional[str]
    password: Optional[str]
    owner: Optional[uuid.UUID]
    template_id: Optional[int]

    obs_host: Optional[str]
    obs_port: Optional[int]
    obs_password: Optional[str]


class TeamOBSRead(BaseModel):
    obs_host: str
    obs_port: int
    obs_password: str


class TeamOBSUpdate(BaseModel):
    obs_host: Optional[str]
    obs_port: Optional[int]
    obs_password: Optional[str]
