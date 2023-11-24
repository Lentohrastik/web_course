import uuid
from fastapi import APIRouter

from src.schemas.team import TeamRead, TeamCreate, TeamUpdate, TeamOBSRead, TeamOBSUpdate


team_router = APIRouter(
    prefix='/team',
    tags=['Team']
)


@team_router.get('/{id}', responses={200: {"model": TeamRead}})
async def get_team_by_id(id: uuid.UUID) -> TeamRead:
    pass


@team_router.post('/', responses={200: {"model": TeamRead}})
async def create_team(team: TeamCreate) -> TeamRead:
    pass


@team_router.patch('/{id}', responses={200: {"model": TeamRead}})
async def updatae_team_by_id(id: uuid.UUID, team: TeamUpdate) -> TeamRead:
    pass


@team_router.delete('/{id}', responses={200: {"model": uuid.UUID}})
async def delete_team_by_id(id: uuid.UUID) -> uuid.UUID:
    pass


@team_router.get('/{id}/obs', responses={200: {"model": TeamOBSRead}})
async def get_obs_config_by_team_id(id: uuid.UUID) -> TeamOBSRead:
    pass


@team_router.patch('/{id}/obs', responses={200: {"model": TeamOBSRead}})
async def updatae_obs_config_by_team_id(id: uuid.UUID, obs_config: TeamOBSUpdate) -> TeamOBSRead:
    pass