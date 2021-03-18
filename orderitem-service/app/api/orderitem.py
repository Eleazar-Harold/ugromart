from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    OrderItemOut,
    OrderItemIn,
    OrderItemUpdate,
)
from app.api import manager
from app.api.service import (
    is_order_present,
    is_productitem_present,
    is_uom_present,
)

orderitemsapi = APIRouter()


@orderitemsapi.post("/", response_model=OrderItemOut, status_code=201)
async def create_orderitems(payload: OrderItemIn):
    if not is_order_present(payload.order_id):
        raise HTTPException(
            status_code=404,
            detail=f"Order with given id:{payload.order_id} not found",
        )

    if not is_productitem_present(payload.productitem_id):
        raise HTTPException(
            status_code=404,
            detail=f"Product item with given id:{payload.productitem_id} not found",
        )

    if not is_uom_present(payload.uom_id):
        raise HTTPException(
            status_code=404,
            detail=f"Unit of measure with given id:{payload.uom_id} not found",
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

    if not is_order_present(payload.order_id):
        raise HTTPException(
            status_code=404,
            detail=f"Order with given id:{payload.order_id} not found",
        )

    if not is_productitem_present(payload.productitem_id):
        raise HTTPException(
            status_code=404,
            detail=f"Product item with given id:{payload.productitem_id} not found",
        )

    if not is_uom_present(payload.uom_id):
        raise HTTPException(
            status_code=404,
            detail=f"Unit of measure with given id:{payload.uom_id} not found",
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
