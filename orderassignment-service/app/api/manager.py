from app.api.models import OrderAssignmentIn
from app.api.db import orderassignments, database


async def create(payload: OrderAssignmentIn):
    query = orderassignments.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get():
    query = orderassignments.select()
    return await database.fetch_all(query=query)


async def get_by(id):
    query = orderassignments.select(orderassignments.c.id == id)
    return await database.fetch_one(query=query)


async def update(id: int, payload: OrderAssignmentIn):
    query = (
        orderassignments.update()
        .where(orderassignments.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = orderassignments.delete().where(orderassignments.c.id == id)
    return await database.execute(query=query)
