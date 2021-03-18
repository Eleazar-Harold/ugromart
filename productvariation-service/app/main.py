from fastapi import FastAPI
from app.api.productvariation import variationsapi
from app.api.db import metadata, database, engine


metadata.create_all(engine)

app = FastAPI(
    openapi_url="/api/v1/variations/openapi.json",
    docs_url="/api/v1/variations/docs",
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(
    variationsapi,
    prefix="/api/v1/variations",
    tags=["variations"],
)
