from app.api.models import ProductItemIn
from app.api.db import productitems, database


async def create(payload: ProductItemIn):
    query = productitems.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get():
    query = productitems.select()
    return await database.fetch_all(query=query)


async def get_by(id):
    query = productitems.select(productitems.c.id == id)
    return await database.fetch_one(query=query)


async def update(id: int, payload: ProductItemIn):
    query = productitems.update().where(productitems.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


async def delete(id: int):
    query = productitems.delete().where(productitems.c.id == id)
    return await database.execute(query=query)
