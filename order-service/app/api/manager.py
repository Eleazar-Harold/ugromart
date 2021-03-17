from app.api.models import OrderIn
from app.api.db import orders, database


async def create(payload: OrderIn):
    query = orders.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get():
    query = orders.select()
    return await database.fetch_all(query=query)


async def get_by(id):
    query = orders.select(orders.c.id == id)
    return await database.fetch_one(query=query)


async def update(id: int, payload: OrderIn):
    query = orders.update().where(orders.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


async def delete(id: int):
    query = orders.delete().where(orders.c.id == id)
    return await database.execute(query=query)
