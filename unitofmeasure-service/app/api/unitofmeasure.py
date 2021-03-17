from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import UomOut, UomIn, UomUpdate
from app.api import manager

uomsapi = APIRouter()


@uomsapi.post("/", response_model=UomOut, status_code=201)
async def create_uom(payload: UomIn):
    uom_id = await manager.create(payload)
    response = {"id": uom_id, **payload.dict()}
    return response


@uomsapi.get("/", response_model=List[UomOut])
async def get_uoms():
    return await manager.get()


@uomsapi.get("/{id}/", response_model=UomOut)
async def get_uom(id: int):
    uom = await manager.get_by(id)
    if not uom:
        raise HTTPException(
            status_code=404,
            detail="Unit of Measure not found",
        )
    return uom


@uomsapi.put("/{id}/", response_model=UomOut)
async def update_uom(id: int, payload: UomUpdate):
    uom = await manager.get_by(id)
    if not uom:
        raise HTTPException(
            status_code=404,
            detail="Unit of Measure not found",
        )

    update_data = payload.dict(exclude_unset=True)

    uom_in_db = UomIn(**uom)
    updated_uom = uom_in_db.copy(update=update_data)
    return await manager.update(id, updated_uom)


@uomsapi.delete("/{id}/", response_model=None)
async def delete_uom(id: int):
    uom = await manager.get_by(id)
    if not uom:
        raise HTTPException(status_code=404, detail="Unit of Measure not found")
    return await manager.delete(id)
