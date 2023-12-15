from typing import List
import uuid
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import SQLAlchemyError
from src.schemas.main_schemas import ErrorSchema, IdRead
from src.services.photo import PhotoService

from src.schemas.photo import PhotoRead, PhotoCreate
from utils.unit_of_work import IUnitOfWork, UnitOfWork


photo_router = APIRouter(
    prefix='/photo',
    tags=['Photo']
)


@photo_router.get('/team/{team_id}', responses={200: {"model": List[PhotoRead]}, 500: {"model": ErrorSchema}})
async def get_photos_by_team_id(team_id: uuid.UUID, uow: IUnitOfWork = Depends(UnitOfWork)) -> List[PhotoRead]:
    try:
        photos = await PhotoService().get_photos_by_team_id(uow, team_id)
        return photos
    except SQLAlchemyError as e:
        raise HTTPException(500, detail=f"Ошибка обращения к базе данных!")
    except:
        raise HTTPException(500, detail=f"Неизвестная ошибка!")


@photo_router.post('/', responses={200: {"model": IdRead}, 500: {"model": ErrorSchema}})
async def create_photo(photo: PhotoCreate, uow: IUnitOfWork = Depends(UnitOfWork)) -> IdRead:
    try:
        photo_id = await PhotoService().create_photo(uow, photo)
        return {"id": photo_id}
    except SQLAlchemyError as e:
        raise HTTPException(500, detail=f"Ошибка обращения к базе данных!")
    except:
        raise HTTPException(500, detail=f"Неизвестная ошибка!")


@photo_router.delete('/{id}', responses={200: {"model": IdRead}, 500: {"model": ErrorSchema}})
async def delete_photo_by_id(id: uuid.UUID, uow: IUnitOfWork = Depends(UnitOfWork)) -> IdRead:
    try:
        photo_id = await PhotoService().delete_photo_by_id(uow, id)
        return {"id": photo_id}
    except SQLAlchemyError:
        raise HTTPException(500, detail=f"Ошибка обращения к базе данных!")
    except:
        raise HTTPException(500, detail=f"Неизвестная ошибка!")
