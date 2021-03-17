from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    DeliveryConfirmationOut,
    DeliveryConfirmationIn,
    DeliveryConfirmationUpdate,
)
from app.api import manager
from app.api.service import is_cast_present

deliveryconfirmationsapi = APIRouter()


@deliveryconfirmationsapi.post(
    "/", response_model=DeliveryConfirmationOut, status_code=201
)
async def create_deliveryconfirmations(payload: DeliveryConfirmationIn):
    # to be revisited
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(
                status_code=404,
                detail=f"Cast with given id:{cast_id} not found",
            )

    confirmation_id = await manager.create(payload)
    response = {"id": confirmation_id, **payload.dict()}
    return response


@deliveryconfirmationsapi.get("/", response_model=List[DeliveryConfirmationOut])
async def get_deliveryconfirmations():
    return await manager.get()


@deliveryconfirmationsapi.get("/{id}/", response_model=DeliveryConfirmationOut)
async def get_deliveryconfirmation(id: int):
    deliveryconfirmation = await manager.get_by(id)
    if not deliveryconfirmation:
        raise HTTPException(
            status_code=404,
            detail="Delivery confirmation not found",
        )
    return deliveryconfirmation


@deliveryconfirmationsapi.put("/{id}/", response_model=DeliveryConfirmationOut)
async def update_deliveryconfirmation(id: int, payload: DeliveryConfirmationUpdate):
    deliveryconfirmation = await manager.get_by(id)
    if not deliveryconfirmation:
        raise HTTPException(
            status_code=404,
            detail="Delivery confirmation not found",
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

    deliveryconfirmation_in_db = DeliveryConfirmationIn(**deliveryconfirmation)
    updated_deliveryconfirmation = deliveryconfirmation_in_db.copy(update=update_data)
    return await manager.update(id, updated_deliveryconfirmation)


@deliveryconfirmationsapi.delete("/{id}/", response_model=None)
async def delete_deliveryconfirmation(id: int):
    deliveryconfirmation = await manager.get_by(id)
    if not deliveryconfirmation:
        raise HTTPException(status_code=404, detail="Delivery confirmation not found")
    return await manager.delete(id)
