from fastapi import FastAPI
from app.api.productitem import productitemsapi
from app.api.db import metadata, database, engine


metadata.create_all(engine)

app = FastAPI(
    openapi_url="/api/v1/productitems/openapi.json",
    docs_url="/api/v1/productitems/docs",
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(
    productitemsapi,
    prefix="/api/v1/productitems",
    tags=["productitems"],
)
