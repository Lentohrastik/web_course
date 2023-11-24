from fastapi import APIRouter

from src.schemas.template import TemplateCreate, TemplateRead, TemplateUpdate


template_router = APIRouter(
    prefix='/photo',
    tags=['Photo']
)


@template_router.get('/{id}', responses={200: {"model": TemplateRead}})
async def get_template_by_id(id: int) -> TemplateRead:
    pass


@template_router.post('/', responses={200: {"model": TemplateRead}})
async def create_template(team: TemplateCreate) -> TemplateRead:
    pass


@template_router.patch('/{id}', responses={200: {"model": TemplateRead}})
async def updatae_template_by_id(id: int, team: TemplateUpdate) -> TemplateRead:
    pass


@template_router.delete('/{id}', responses={200: {"model": int}})
async def delete_template_by_id(id: int) -> int:
    pass