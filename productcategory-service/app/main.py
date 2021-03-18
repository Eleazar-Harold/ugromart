from fastapi import FastAPI
from app.api.productcategory import categoriesapi
from app.api.db import metadata, database, engine


metadata.create_all(engine)

app = FastAPI(
    openapi_url="/api/v1/categories/openapi.json",
    docs_url="/api/v1/categories/docs",
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(
    categoriesapi,
    prefix="/api/v1/categories",
    tags=["categories"],
)
