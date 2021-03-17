from fastapi import FastAPI
from app.api.deliveryconfirmation import deliveryconfirmationsapi
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(
    openapi_url="/api/v1/confirmations/openapi.json",
    docs_url="/api/v1/confirmations/docs",
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(
    deliveryconfirmationsapi,
    prefix="/api/v1/confirmations",
    tags=["confirmations"],
)
