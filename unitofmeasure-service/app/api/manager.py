from app.api.models import UomIn, UomOut, UomUpdate
from app.api.db import unitofmeasures, database


async def create(payload: UomIn):
    query = unitofmeasures.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get():
    query = unitofmeasures.select()
    return await database.fetch_all(query=query)


async def get_by(id):
    query = unitofmeasures.select(unitofmeasures.c.id == id)
    return await database.fetch_one(query=query)


async def update(id: int, payload: UomIn):
    query = (
        unitofmeasures.update().where(unitofmeasures.c.id == id).values(**payload.dict())
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = unitofmeasures.delete().where(unitofmeasures.c.id == id)
    return await database.execute(query=query)
