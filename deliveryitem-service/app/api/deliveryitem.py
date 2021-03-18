from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    DeliveryItemOut,
    DeliveryItemIn,
    DeliveryItemUpdate,
)
from app.api import manager
from app.api.service import (
    is_delivery_present,
    is_productitem_present,
    is_uom_present,
)

deliveryitemsapi = APIRouter()


@deliveryitemsapi.post("/", response_model=DeliveryItemOut, status_code=201)
async def create_deliveryitems(payload: DeliveryItemIn):
    if not is_delivery_present(payload.delivery_id):
        raise HTTPException(
            status_code=404,
            detail=f"Delivery with given id:{payload.delivery_id} not found",
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

    deliveryitem_id = await manager.create(payload)
    response = {"id": deliveryitem_id, **payload.dict()}
    return response


@deliveryitemsapi.get("/", response_model=List[DeliveryItemOut])
async def get_deliveryitems():
    return await manager.get()


@deliveryitemsapi.get("/{id}/", response_model=DeliveryItemOut)
async def get_deliveryitem(id: int):
    deliveryitem = await manager.get_by(id)
    if not deliveryitem:
        raise HTTPException(
            status_code=404,
            detail="Delivery item not found",
        )
    return deliveryitem


@deliveryitemsapi.put("/{id}/", response_model=DeliveryItemOut)
async def update_deliveryitem(id: int, payload: DeliveryItemUpdate):
    deliveryitem = await manager.get_by(id)
    if not deliveryitem:
        raise HTTPException(
            status_code=404,
            detail="Delivery item not found",
        )

    update_data = payload.dict(exclude_unset=True)

    if not is_delivery_present(payload.delivery_id):
        raise HTTPException(
            status_code=404,
            detail=f"Delivery with given id:{payload.delivery_id} not found",
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

    deliveryitem_in_db = DeliveryItemIn(**deliveryitem)
    updated_deliveryitem = deliveryitem_in_db.copy(update=update_data)
    return await manager.update(id, updated_deliveryitem)


@deliveryitemsapi.delete("/{id}/", response_model=None)
async def delete_deliveryitem(id: int):
    delivery = await manager.get_by(id)
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery item not found")
    return await manager.delete(id)
