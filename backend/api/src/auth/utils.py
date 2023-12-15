from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

import smtplib
from email.message import EmailMessage
from src.config import SMTP_HOST, SMTP_PASS, SMTP_PORT, SMTP_USER


from src.models import User
from database import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

def get_email_template_dashboard(username: str, email: str, token: str):
    email = EmailMessage()
    email['Subject'] = 'Сброс пароля!'
    email['From'] = SMTP_USER
    email['To'] = email

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        f'<h7>Token: {token}</h7>'
        '</div>',
        subtype='html'
    )
    return email


def send_email_report_dashboard(username: str, email: str, token: str):
    email = get_email_template_dashboard(username, email, token)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        print(server.login(SMTP_USER, SMTP_PASS))
        server.send_message(email)