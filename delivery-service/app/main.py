from fastapi import FastAPI
from app.api.delivery import deliveries
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(
    openapi_url="/api/v1/deliveries/openapi.json",
    docs_url="/api/v1/deliveries/docs",
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(
    deliveries,
    prefix="/api/v1/deliveries",
    tags=["deliveries"],
)
