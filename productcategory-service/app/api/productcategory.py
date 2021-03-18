from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    CategoryOut,
    CategoryIn,
    CategoryUpdate,
)
from app.api import manager
from app.api.service import is_cast_present

categoriesapi = APIRouter()


@categoriesapi.post("/", response_model=CategoryOut, status_code=201)
async def create_category(payload: CategoryIn):
    # to be revisited
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(
                status_code=404,
                detail=f"Cast with given id:{cast_id} not found",
            )

    category_id = await manager.create(payload)
    response = {"id": category_id, **payload.dict()}
    return response


@categoriesapi.get("/", response_model=List[CategoryOut])
async def get_categories():
    return await manager.get()


@categoriesapi.get("/{id}/", response_model=CategoryOut)
async def get_category(id: int):
    category = await manager.get_by(id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )
    return category


@categoriesapi.put("/{id}/", response_model=CategoryOut)
async def update_category(id: int, payload: CategoryUpdate):
    category = await manager.get_by(id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    update_data = payload.dict(exclude_unset=True)

    # to be revisited
    if "casts_id" in update_data:
        for cast_id in payload.casts_id:
            if not is_cast_present(cast_id):
                raise HTTPException(
                    status_code=404,
                    detail=f"Cast with given id:{cast_id} not found",
                )

    category_in_db = CategoryIn(**category)
    updated_category = category_in_db.copy(update=update_data)
    return await manager.update(id, updated_category)


@categoriesapi.delete("/{id}/", response_model=None)
async def delete_category(id: int):
    category = await manager.get_by(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return await manager.delete(id)
