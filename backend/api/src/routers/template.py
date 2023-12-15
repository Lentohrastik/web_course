from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from src.schemas.main_schemas import ErrorSchema
from services.template import TemplateService

from src.schemas.template import TemplateRead
from src.utils.unit_of_work import IUnitOfWork, UnitOfWork


template_router = APIRouter(
    prefix='/template',
    tags=['Template']
)


@template_router.get('/all', responses={200: {"model": List[TemplateRead]}, 500: {"model": ErrorSchema}})
async def get_template_by_id(uow: IUnitOfWork = Depends(UnitOfWork)) -> List[TemplateRead]:
    try:
        templates = await TemplateService().get_all_templates(uow)
        return templates
    except SQLAlchemyError:
        raise HTTPException(500, detail=f"Ошибка обращения к базе данных!")
    except:
        raise HTTPException(500, detail=f"Неизвестная ошибка!")


@template_router.get('/team/{team_id}', responses={200: {"model": TemplateRead}, 500: {"model": ErrorSchema}})
async def get_template_by_id(team_id: uuid.UUID, uow: IUnitOfWork = Depends(UnitOfWork)) -> TemplateRead:
    try:
        template = await TemplateService().get_template_by_team_id(uow, team_id)
        return template
    except SQLAlchemyError:
        raise HTTPException(500, detail=f"Ошибка обращения к базе данных!")
    except:
        raise HTTPException(500, detail=f"Неизвестная ошибка!")
