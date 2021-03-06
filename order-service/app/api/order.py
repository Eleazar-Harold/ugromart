from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    OrderOut,
    OrderIn,
    OrderUpdate,
)
from app.api import manager

ordersapi = APIRouter()


@ordersapi.post("/", response_model=OrderOut, status_code=201)
async def create_orders(payload: OrderIn):
    order_id = await manager.create(payload)
    response = {"id": order_id, **payload.dict()}
    return response


@ordersapi.get("/", response_model=List[OrderOut])
async def get_orders():
    return await manager.get()


@ordersapi.get("/{id}/", response_model=OrderOut)
async def get_order(id: int):
    order = await manager.get_by(id)
    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )
    return order


@ordersapi.put("/{id}/", response_model=OrderOut)
async def update_order(id: int, payload: OrderUpdate):
    order = await manager.get_by(id)
    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    update_data = payload.dict(exclude_unset=True)

    order_in_db = OrderIn(**order)
    updated_order = order_in_db.copy(update=update_data)
    return await manager.update(id, updated_order)


@ordersapi.delete("/{id}/", response_model=None)
async def delete_order(id: int):
    order = await manager.get_by(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return await manager.delete(id)
