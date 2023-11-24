import uvicorn

from config import API_PORT

from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi

from models import User
from schemas.user import UserCreate, UserRead, UserUpdate
from auth.manager import get_user_manager
from auth.router import auth_backend, authentication, current_active_user
from fastapi.middleware.cors import CORSMiddleware

from routers.team import team_router
from routers.photo import photo_router
from routers.template import template_router
from routers.obs_scene import scene_router

from fastapi_users.router import get_auth_router, get_register_router, get_reset_password_router, get_users_router


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Auto Caption System API",
        version="2.5.0",
        description="It is API for Auto Caption System.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI(title='Auto Caption System')
app.openapi = custom_openapi

app.include_router(
    get_auth_router(auth_backend, get_user_manager, authentication.authenticator),
    prefix="/auth",
    tags=["Auth"]
)
app.include_router(
    get_register_router(get_user_manager, UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
app.include_router(
    get_reset_password_router(get_user_manager),
    prefix="/auth",
    tags=["Auth"],
)
app.include_router(
    get_users_router(get_user_manager, UserRead, UserUpdate, authentication.authenticator),
    prefix="/users",
    tags=["User"],
)
app.include_router(team_router)
app.include_router(photo_router)
app.include_router(template_router)
app.include_router(scene_router)

origins = [
 #   "http://localhost:8081/auth",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["*"],
    expose_headers=["*"]
    # allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
    #                "Authorization", "Access-Control-Allow-Origin"],
)

@app.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}!"

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=API_PORT)