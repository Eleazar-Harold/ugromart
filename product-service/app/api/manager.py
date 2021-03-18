from app.api.models import ProductIn
from app.api.db import products, database


async def create(payload: ProductIn):
    query = products.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get():
    query = products.select()
    return await database.fetch_all(query=query)


async def get_by(id):
    query = products.select(products.c.id == id)
    return await database.fetch_one(query=query)


async def update(id: int, payload: ProductIn):
    query = products.update().where(products.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


async def delete(id: int):
    query = products.delete().where(products.c.id == id)
    return await database.execute(query=query)
