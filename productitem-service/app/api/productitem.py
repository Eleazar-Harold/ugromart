from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    ProductItemOut,
    ProductItemIn,
    ProductItemUpdate,
)
from app.api import manager
from app.api.service import is_cast_present

productitemsapi = APIRouter()


@productitemsapi.post("/", response_model=ProductItemOut, status_code=201)
async def create_productitems(payload: ProductItemIn):
    # to be revisited
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(
                status_code=404,
                detail=f"Cast with given id:{cast_id} not found",
            )

    productitem_id = await manager.create(payload)
    response = {"id": productitem_id, **payload.dict()}
    return response


@productitemsapi.get("/", response_model=List[ProductItemOut])
async def get_productitems():
    return await manager.get()


@productitemsapi.get("/{id}/", response_model=ProductItemOut)
async def get_productitem(id: int):
    productitem = await manager.get_by(id)
    if not productitem:
        raise HTTPException(
            status_code=404,
            detail="Order item not found",
        )
    return productitem


@productitemsapi.put("/{id}/", response_model=ProductItemOut)
async def update_productitem(id: int, payload: ProductItemUpdate):
    productitem = await manager.get_by(id)
    if not productitem:
        raise HTTPException(
            status_code=404,
            detail="Order item not found",
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

    productitem_in_db = ProductItemIn(**productitem)
    updated_productitem = productitem_in_db.copy(update=update_data)
    return await manager.update(id, updated_productitem)


@productitemsapi.delete("/{id}/", response_model=None)
async def delete_productitem(id: int):
    order = await manager.get_by(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order item not found")
    return await manager.delete(id)
