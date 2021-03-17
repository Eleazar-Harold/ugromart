from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import DeliveryOut, DeliveryIn, DeliveryUpdate
from app.api import manager
from app.api.service import is_cast_present

deliveries = APIRouter()


@deliveries.post("/", response_model=DeliveryOut, status_code=201)
async def create_delivery(payload: DeliveryIn):
    # to be revisited
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(
                status_code=404,
                detail=f"Cast with given id:{cast_id} not found",
            )

    delivery_id = await manager.create(payload)
    response = {"id": delivery_id, **payload.dict()}
    return response


@deliveries.get("/", response_model=List[DeliveryOut])
async def get_deliveries():
    return await manager.get()


@deliveries.get("/{id}/", response_model=DeliveryOut)
async def get_delivery(id: int):
    delivery = await manager.get_by(id)
    if not delivery:
        raise HTTPException(
            status_code=404,
            detail="Delivery not found",
        )
    return delivery


@deliveries.put("/{id}/", response_model=DeliveryOut)
async def update_delivery(id: int, payload: DeliveryUpdate):
    delivery = await manager.get_by(id)
    if not delivery:
        raise HTTPException(
            status_code=404,
            detail="Delivery not found",
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

    delivery_in_db = DeliveryIn(**delivery)
    updated_delivery = delivery_in_db.copy(update=update_data)
    return await manager.update(id, updated_delivery)


@deliveries.delete("/{id}/", response_model=None)
async def delete_delivery(id: int):
    delivery = await manager.get_by(id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return await manager.delete(id)
