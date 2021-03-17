from app.api.models import OrderItemIn
from app.api.db import orderitems, database


async def create(payload: OrderItemIn):
    query = orderitems.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get():
    query = orderitems.select()
    return await database.fetch_all(query=query)


async def get_by(id):
    query = orderitems.select(orderitems.c.id == id)
    return await database.fetch_one(query=query)


async def update(id: int, payload: OrderItemIn):
    query = orderitems.update().where(orderitems.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


async def delete(id: int):
    query = orderitems.delete().where(orderitems.c.id == id)
    return await database.execute(query=query)
