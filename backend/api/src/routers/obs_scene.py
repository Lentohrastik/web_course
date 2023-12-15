from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException
from src.utils.unit_of_work import IUnitOfWork, UnitOfWork

from src.schemas.main_schemas import ErrorSchema, IdRead
from services.obs_scene import SceneService
from src.schemas.obs_scene import SceneCreate, SceneRead


scene_router = APIRouter(
    prefix='/obs_scene',
    tags=['OBS scene']
)


@scene_router.get('/team/{team_id}', responses={200: {"model": List[SceneRead]}, 500: {"model": ErrorSchema}})
async def get_scenes_by_team_id(team_id: uuid.UUID, uow: IUnitOfWork = Depends(UnitOfWork)) -> List[SceneRead]:
    scenes = await SceneService().get_scenes_by_team_id(uow, team_id)
    return scenes


@scene_router.post('/', responses={200: {"model": IdRead}, 500: {"model": ErrorSchema}})
async def create_scene(scene: SceneCreate, uow: IUnitOfWork = Depends(UnitOfWork)) -> IdRead:
    scene_id = await SceneService().create_scene(uow, scene)
    return {"id": scene_id}


@scene_router.delete('/{id}', responses={200: {"model": IdRead}, 500: {"model": ErrorSchema}})
async def delete_scene_by_id(id: uuid.UUID, uow: IUnitOfWork = Depends(UnitOfWork)) -> IdRead:
    scene_id = await SceneService().delete_scene_by_id(uow, id)
    return {"id": scene_id}


@scene_router.delete('/team/{team_id}', responses={200: {"model": List[IdRead]}, 500: {"model": ErrorSchema}})
async def delete_scenes_by_team_id(team_id: uuid.UUID, uow: IUnitOfWork = Depends(UnitOfWork)) -> List[IdRead]:
    scene_ids = await SceneService().delete_scenes_by_team_id(uow, team_id)
    return scene_ids
