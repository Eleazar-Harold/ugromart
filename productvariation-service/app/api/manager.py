from app.api.models import VariationIn, ProductVariationIn
from app.api.db import variations, database, productvariations


async def create(payload: VariationIn):
    query = variations.insert().values(**payload.dict())
    return await database.execute(query=query)


async def create(payload: ProductVariationIn):
    query = productvariations.insert().values(**payload.dict())
    return await database.execute(query=query)


async def variations():
    query = variations.select()
    return await database.fetch_all(query=query)


async def products_variations():
    query = productvariations.select()
    return await database.fetch_all(query=query)


async def variation_by(id: int):
    query = variations.select(variations.c.id == id)
    return await database.fetch_one(query=query)


async def get_by(variation_id: int, product_id: int):
    query = productvariations.select(
        productvariations.c.variation_id == variation_id,
        productvariations.c.product_id == product_id,
    )
    return await database.fetch_one(query=query)


async def update(id: int, payload: VariationIn):
    query = variations.update().where(variations.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


async def delete(id: int):
    query = variations.delete().where(variations.c.id == id)
    return await database.execute(query=query)
