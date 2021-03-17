from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    OrderItemOut,
    OrderItemIn,
    OrderItemUpdate,
)
from app.api import manager
from app.api.service import is_cast_present

orderitemsapi = APIRouter()


@orderitemsapi.post("/", response_model=OrderItemOut, status_code=201)
async def create_orderitems(payload: OrderItemIn):
    # to be revisited
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(
                status_code=404,
                detail=f"Cast with given id:{cast_id} not found",
            )

    orderitem_id = await manager.create(payload)
    response = {"id": orderitem_id, **payload.dict()}
    return response


@orderitemsapi.get("/", response_model=List[OrderItemOut])
async def get_orderitems():
    return await manager.get()


@orderitemsapi.get("/{id}/", response_model=OrderItemOut)
async def get_orderitem(id: int):
    orderitem = await manager.get_by(id)
    if not orderitem:
        raise HTTPException(
            status_code=404,
            detail="Order item not found",
        )
    return orderitem


@orderitemsapi.put("/{id}/", response_model=OrderItemOut)
async def update_orderitem(id: int, payload: OrderItemUpdate):
    orderitem = await manager.get_by(id)
    if not orderitem:
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

    orderitem_in_db = OrderItemIn(**orderitem)
    updated_orderitem = orderitem_in_db.copy(update=update_data)
    return await manager.update(id, updated_orderitem)


@orderitemsapi.delete("/{id}/", response_model=None)
async def delete_orderitem(id: int):
    order = await manager.get_by(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order item not found")
    return await manager.delete(id)
