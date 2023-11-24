import uuid
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend#, BearerTransport
from fastapi_users.authentication import JWTStrategy

from auth.manager import get_user_manager
from src.models import User
from config import SECRET_AUTH

cookie_transport = CookieTransport(cookie_name="ACS_cookie", cookie_max_age=3600, cookie_httponly=False)
#bearer_transport = BearerTransport('auth/login')


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=10)

auth_backend = AuthenticationBackend(
    name="ACS",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

authentication = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = authentication.current_user(active=True)