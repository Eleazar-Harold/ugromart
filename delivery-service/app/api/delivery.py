from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import DeliveryOut, DeliveryIn, DeliveryUpdate
from app.api import manager
from app.api.service import (
    is_deliverystatus_present,
    is_order_present,
    is_payment_present,
)

deliveriesapi = APIRouter()


@deliveriesapi.post("/", response_model=DeliveryOut, status_code=201)
async def create_delivery(payload: DeliveryIn):
    if not is_deliverystatus_present(payload.delivery_status_id):
        raise HTTPException(
            status_code=404,
            detail=f"Delivery status with given id:{payload.delivery_status_id} not found",
        )

    if not is_order_present(payload.order_id):
        raise HTTPException(
            status_code=404,
            detail=f"Order with given id:{payload.order_id} not found",
        )

    for p_id in payload.payments_id:
        if not is_payment_present(p_id):
            raise HTTPException(
                status_code=404,
                detail=f"Payment with given id:{pp_id} not found",
            )

    delivery_id = await manager.create(payload)
    response = {"id": delivery_id, **payload.dict()}
    return response


@deliveriesapi.get("/", response_model=List[DeliveryOut])
async def get_deliveries():
    return await manager.get()


@deliveriesapi.get("/{id}/", response_model=DeliveryOut)
async def get_delivery(id: int):
    delivery = await manager.get_by(id)
    if not delivery:
        raise HTTPException(
            status_code=404,
            detail="Delivery not found",
        )
    return delivery


@deliveriesapi.put("/{id}/", response_model=DeliveryOut)
async def update_delivery(id: int, payload: DeliveryUpdate):
    delivery = await manager.get_by(id)
    if not delivery:
        raise HTTPException(
            status_code=404,
            detail="Delivery not found",
        )

    update_data = payload.dict(exclude_unset=True)

    if not is_deliverystatus_present(payload.delivery_status_id):
        raise HTTPException(
            status_code=404,
            detail=f"Delivery status with given id:{payload.delivery_status_id} not found",
        )

    if not is_order_present(payload.order_id):
        raise HTTPException(
            status_code=404,
            detail=f"Order with given id:{payload.order_id} not found",
        )

    for p_id in payload.payments_id:
        if not is_payment_present(p_id):
            raise HTTPException(
                status_code=404,
                detail=f"Payment with given id:{pp_id} not found",
            )

    delivery_in_db = DeliveryIn(**delivery)
    updated_delivery = delivery_in_db.copy(update=update_data)
    return await manager.update(id, updated_delivery)


@deliveriesapi.delete("/{id}/", response_model=None)
async def delete_delivery(id: int):
    delivery = await manager.get_by(id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return await manager.delete(id)
