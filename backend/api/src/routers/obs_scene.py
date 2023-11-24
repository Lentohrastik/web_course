import uuid
from fastapi import APIRouter

from src.schemas.obs_scene import SceneCreate, SceneRead, SceneUpdate


scene_router = APIRouter(
    prefix='/obs_scene',
    tags=['OBS scene']
)


@scene_router.get('/{id}', responses={200: {"model": SceneRead}})
async def get_scene_by_id(id: uuid.UUID) -> SceneRead:
    pass


@scene_router.post('/', responses={200: {"model": SceneRead}})
async def create_scene(team: SceneCreate) -> SceneRead:
    pass


@scene_router.patch('/{id}', responses={200: {"model": SceneRead}})
async def updatae_scene_by_id(id: uuid.UUID, team: SceneUpdate) -> SceneRead:
    pass


@scene_router.delete('/{id}', responses={200: {"model": uuid.UUID}})
async def delete_scene_by_id(id: uuid.UUID) -> uuid.UUID:
    pass
