from app.api.models import CategoryIn, ProductCategoryIn
from app.api.db import categories, database, productscategories


async def create(payload: CategoryIn):
    query = categories.insert().values(**payload.dict())
    return await database.execute(query=query)


async def create(payload: ProductCategoryIn):
    query = productscategories.insert().values(**payload.dict())
    return await database.execute(query=query)


async def categories():
    query = categories.select()
    return await database.fetch_all(query=query)


async def product_categories():
    query = productscategories.select()
    return await database.fetch_all(query=query)


async def category_by(id: int):
    query = categories.select(categories.c.id == id)
    return await database.fetch_one(query=query)


async def get_by(category_id: int, product_id: int):
    query = productscategories.select(
        productscategories.c.category_id == category_id,
        productscategories.c.product_id == product_id,
    )
    return await database.fetch_one(query=query)


async def update(id: int, payload: CategoryIn):
    query = categories.update().where(categories.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


async def delete(id: int):
    query = categories.delete().where(categories.c.id == id)
    return await database.execute(query=query)
