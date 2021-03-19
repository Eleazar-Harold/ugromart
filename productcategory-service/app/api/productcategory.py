from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    CategoryOut,
    CategoryIn,
    CategoryUpdate,
    ProductCategoryOut,
    ProductCategoryIn,
)
from app.api import manager
from app.api.service import (
    is_category_present,
    is_product_present,
    get_category,
    get_product,
)

categoriesapi = APIRouter()


@categoriesapi.post("/", response_model=CategoryOut, status_code=201)
async def create_category(payload: CategoryIn):
    category_id = await manager.create(payload)
    response = {"id": category_id, **payload.dict()}
    return response


@categoriesapi.post("/products", response_model=ProductCategoryOut, status_code=201)
async def create_productcategory(payload: ProductCategoryIn):
    if not is_category_present(payload.category_id):
        raise HTTPException(
            status_code=404,
            detail=f"Category with given id:{payload.category_id} not found",
        )

    if not is_product_present(payload.product_id):
        raise HTTPException(
            status_code=404,
            detail=f"Product with given id:{payload.product_id} not found",
        )

    results = await manager.get_by(
        payload.category_id,
        payload.product_id,
    )
    if results:
        return {
            "category": get_category(results.category_id),
            "product": get_product(results.product_id),
        }
    results = await manager.create(payload)
    return {
        "category": get_category(results.category_id),
        "product": get_product(results.product_id),
    }


@categoriesapi.get("/", response_model=List[CategoryOut])
async def get_categories():
    return await manager.categories()


@categoriesapi.get("/products", response_model=List[ProductCategoryOut])
async def get_productcategories():
    return await manager.product_categories()


@categoriesapi.get("/{id}/", response_model=CategoryOut)
async def get_category(id: int):
    category = await manager.category_by(id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )
    return category


@categoriesapi.put("/{id}/", response_model=CategoryOut)
async def update_category(id: int, payload: CategoryUpdate):
    category = await manager.category_by(id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    update_data = payload.dict(exclude_unset=True)

    category_in_db = CategoryIn(**category)
    updated_category = category_in_db.copy(update=update_data)
    return await manager.update(id, updated_category)


@categoriesapi.delete("/{id}/", response_model=None)
async def delete_category(id: int):
    category = await manager.category_by(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return await manager.delete(id)
