from app.api.models import DeliveryItemIn
from app.api.db import deliveryitems, database


async def create(payload: DeliveryItemIn):
    query = deliveryitems.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get():
    query = deliveryitems.select()
    return await database.fetch_all(query=query)


async def get_by(id):
    query = deliveryitems.select(deliveryitems.c.id == id)
    return await database.fetch_one(query=query)


async def update(id: int, payload: DeliveryItemIn):
    query = (
        deliveryitems.update().where(deliveryitems.c.id == id).values(**payload.dict())
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = deliveryitems.delete().where(deliveryitems.c.id == id)
    return await database.execute(query=query)
