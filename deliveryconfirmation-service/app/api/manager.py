from app.api.models import DeliveryConfirmationIn
from app.api.db import deliveryconfirmations, database


async def create(payload: DeliveryConfirmationIn):
    query = deliveryconfirmations.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get():
    query = deliveryconfirmations.select()
    return await database.fetch_all(query=query)


async def get_by(id):
    query = deliveryconfirmations.select(deliveryconfirmations.c.id == id)
    return await database.fetch_one(query=query)


async def update(id: int, payload: DeliveryConfirmationIn):
    query = (
        deliveryconfirmations.update()
        .where(deliveryconfirmations.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = deliveryconfirmations.delete().where(deliveryconfirmations.c.id == id)
    return await database.execute(query=query)
