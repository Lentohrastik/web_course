from fastapi import APIRouter, Depends, HTTPException
from src.auth.manager import get_user_manager
from src.schemas.main_schemas import ErrorSchema, IdRead
from src.auth.router import authentication, current_active_user
from services.user import UsersService

from sqlalchemy.exc import SQLAlchemyError
from fastapi_users.router import get_users_router

from src.schemas.user import UserRead, UserUpdate
from utils.unit_of_work import IUnitOfWork, UnitOfWork


user_router = get_users_router(get_user_manager,
                               UserRead, UserUpdate,
                               authentication.authenticator)

