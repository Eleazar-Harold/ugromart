from app.api.models import CategoryIn
from app.api.db import categories, database


async def create(payload: CategoryIn):
    query = categories.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get():
    query = categories.select()
    return await database.fetch_all(query=query)


async def get_by(id):
    query = categories.select(categories.c.id == id)
    return await database.fetch_one(query=query)


async def update(id: int, payload: CategoryIn):
    query = categories.update().where(categories.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


async def delete(id: int):
    query = categories.delete().where(categories.c.id == id)
    return await database.execute(query=query)
