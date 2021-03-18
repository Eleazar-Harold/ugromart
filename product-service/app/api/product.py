from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    ProductOut,
    ProductIn,
    ProductUpdate,
)
from app.api import manager

productsapi = APIRouter()


@productsapi.post("/", response_model=ProductOut, status_code=201)
async def create_products(payload: ProductIn):
    product_id = await manager.create(payload)
    response = {"id": product_id, **payload.dict()}
    return response


@productsapi.get("/", response_model=List[ProductOut])
async def get_products():
    return await manager.get()


@productsapi.get("/{id}/", response_model=ProductOut)
async def get_product(id: int):
    product = await manager.get_by(id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )
    return product


@productsapi.put("/{id}/", response_model=ProductOut)
async def update_product(id: int, payload: ProductUpdate):
    product = await manager.get_by(id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    update_data = payload.dict(exclude_unset=True)

    product_in_db = ProductIn(**product)
    updated_product = product_in_db.copy(update=update_data)
    return await manager.update(id, updated_product)


@productsapi.delete("/{id}/", response_model=None)
async def delete_product(id: int):
    product = await manager.get_by(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return await manager.delete(id)
