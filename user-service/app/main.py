import os
import databases
import sqlalchemy
from fastapi import FastAPI, Request, Depends, Response
from fastapi_users import FastAPIUsers, models
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

DATABASE_URL = DATABASE_URI = os.getenv("DATABASE_URI")
SECRET = os.getenv("SECRET")


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


database = databases.Database(DATABASE_URL)
Base: DeclarativeMeta = declarative_base()


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


engine = sqlalchemy.create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


def after_verification_request(user: UserDB, token: str, request: Request):
    print(f"Verification requested for user {user.id}. Verification token: {token}")


jwt_authentication = JWTAuthentication(
    secret=SECRET,
    lifetime_seconds=3600,
    tokenUrl="/auth/jwt/login",
)


@router.post("/auth/jwt/refresh")
async def refresh_jwt(
    response: Response, user=Depends(fastapi_users.get_current_active_user)
):
    return await jwt_authentication.get_login_response(user, response)


app = FastAPI(
    openapi_url="/api/v1/auth/openapi.json",
    docs_url="/api/v1/auth/docs",
)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

app.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix="/api/v1/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(on_after_register),
    prefix="/api/v1/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(
        SECRET,
        after_forgot_password=on_after_forgot_password,
    ),
    prefix="/api/v1/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(
        SECRET, after_verification_request=after_verification_request
    ),
    prefix="/api/v1/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(),
    prefix="/api/v1/auth/users",
    tags=["users"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
