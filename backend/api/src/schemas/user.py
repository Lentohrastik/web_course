import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str
    template_id: int
    obs_host: str
    obs_port: int
    obs_password: str


class UserCreate(schemas.BaseUserCreate):
    username: str
    template_id: int = 0
    obs_host: str = '127.0.0.1'
    obs_port: int = 4455
    obs_password: str = ''


class UserUpdate(schemas.BaseUserUpdate):
    username: str = None
    template_id: int = None
    obs_host: str = None
    obs_port: int = None
    obs_password: str = None