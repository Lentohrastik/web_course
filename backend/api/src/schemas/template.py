from pydantic import BaseModel

class TemplateRead(BaseModel):
    id: int
    name: str


class TemplateCreate(BaseModel):
    name: str


class TemplateUpdate(BaseModel):
    name: str