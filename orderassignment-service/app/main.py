from fastapi import FastAPI
from app.api.orderassignment import orderassignmentsapi
from app.api.db import metadata, database, engine


metadata.create_all(engine)

app = FastAPI(
    openapi_url="/api/v1/orderassignments/openapi.json",
    docs_url="/api/v1/orderassignments/docs",
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(
    orderassignmentsapi,
    prefix="/api/v1/orderassignments",
    tags=["orderassignments"],
)
