import uuid
from fastapi import APIRouter

from src.schemas.photo import PhotoRead, PhotoCreate, PhotoUpdate


photo_router = APIRouter(
    prefix='/photo',
    tags=['Photo']
)


@photo_router.get('/{id}', responses={200: {"model": PhotoRead}})
async def get_photo_by_id(id: uuid.UUID) -> PhotoRead:
    pass


@photo_router.post('/', responses={200: {"model": PhotoRead}})
async def create_photo(team: PhotoCreate) -> PhotoRead:
    pass


@photo_router.patch('/{id}', responses={200: {"model": PhotoRead}})
async def updatae_photo_by_id(id: uuid.UUID, team: PhotoUpdate) -> PhotoRead:
    pass


@photo_router.delete('/{id}', responses={200: {"model": uuid.UUID}})
async def delete_photo_by_id(id: uuid.UUID) -> uuid.UUID:
    pass