from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    DeliveryConfirmationOut,
    DeliveryConfirmationIn,
    DeliveryConfirmationUpdate,
)
from app.api import manager
from app.api.service import (
    get_delivery,
    is_delivery_present,
)

confirmationsapi = APIRouter()


@confirmationsapi.post("/", response_model=DeliveryConfirmationOut, status_code=201)
async def create_deliveryconfirmations(payload: DeliveryConfirmationIn):
    if not is_delivery_present(payload.delivery_id):
        raise HTTPException(
            status_code=404,
            detail=f"Delivery with given id:{payload.delivery_id} not found",
        )

    confirmation_id = await manager.create(payload)
    response = {"id": confirmation_id, **payload.dict()}
    return response


@confirmationsapi.get("/", response_model=List[DeliveryConfirmationOut])
async def get_deliveryconfirmations():
    return await manager.get()


@confirmationsapi.get("/{id}/", response_model=DeliveryConfirmationOut)
async def get_deliveryconfirmation(id: int):
    deliveryconfirmation = await manager.get_by(id)
    if not deliveryconfirmation:
        raise HTTPException(
            status_code=404,
            detail="Delivery confirmation not found",
        )
    return deliveryconfirmation


@confirmationsapi.put("/{id}/", response_model=DeliveryConfirmationOut)
async def update_deliveryconfirmation(id: int, payload: DeliveryConfirmationUpdate):
    deliveryconfirmation = await manager.get_by(id)
    if not deliveryconfirmation:
        raise HTTPException(
            status_code=404,
            detail="Delivery confirmation not found",
        )

    update_data = payload.dict(exclude_unset=True)

    if not is_delivery_present(payload.delivery_id):
        raise HTTPException(
            status_code=404,
            detail=f"Delivery with given id:{payload.delivery_id} not found",
        )

    deliveryconfirmation_in_db = DeliveryConfirmationIn(**deliveryconfirmation)
    updated_deliveryconfirmation = deliveryconfirmation_in_db.copy(update=update_data)
    return await manager.update(id, updated_deliveryconfirmation)


@confirmationsapi.delete("/{id}/", response_model=None)
async def delete_deliveryconfirmation(id: int):
    deliveryconfirmation = await manager.get_by(id)
    if not deliveryconfirmation:
        raise HTTPException(status_code=404, detail="Delivery confirmation not found")
    return await manager.delete(id)
