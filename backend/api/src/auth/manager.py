from typing import Optional
import uuid

from fastapi import BackgroundTasks, Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from src.models import User
from auth.utils import get_user_db, send_email_report_dashboard

from config import SECRET_AUTH


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH
    

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
    
    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        # background_task = BackgroundTasks()
        # background_task.add_task(send_email_report_dashboard, user.username, user.email, token)
        # send_email_report_dashboard(user.username, user.email, token)
        print(f"User got token! {token}")
    



async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)