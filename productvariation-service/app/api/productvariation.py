from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    VariationOut,
    VariationIn,
    VariationUpdate,
    ProductVariationOut,
    ProductVariationIn,
)
from app.api import manager
from app.api.service import (
    is_variation_present,
    is_product_present,
    get_variation,
    get_product,
)

variationsapi = APIRouter()


@variationsapi.post("/", response_model=VariationOut, status_code=201)
async def create_variation(payload: VariationIn):
    variation_id = await manager.create(payload)
    response = {"id": variation_id, **payload.dict()}
    return response


@variationsapi.post("/", response_model=ProductVariationOut, status_code=201)
async def create_productvariation(payload: ProductVariationIn):
    if not is_variation_present(payload.variation_id):
        raise HTTPException(
            status_code=404,
            detail=f"Variation with given id:{payload.variation_id} not found",
        )

    if not is_product_present(payload.product_id):
        raise HTTPException(
            status_code=404,
            detail=f"Product with given id:{payload.product_id} not found",
        )

    results = await manager.get_by(
        payload.variation_id,
        payload.product_id,
    )
    if results:
        return {
            "variation": get_variation(results.variation_id),
            "product": get_product(results.product_id),
        }
    results = await manager.create(payload)
    return {
        "variation": get_variation(results.variation_id),
        "product": get_product(results.product_id),
    }


@variationsapi.get("/", response_model=List[VariationOut])
async def get_variations():
    return await manager.variations()


@variationsapi.get("/", response_model=List[ProductVariationOut])
async def get_productvariations():
    return await manager.productvariations()


@variationsapi.get("/{id}/", response_model=VariationOut)
async def get_variation(id: int):
    variation = await manager.variation_by(id)
    if not variation:
        raise HTTPException(
            status_code=404,
            detail="Variation not found",
        )
    return variation


@variationsapi.put("/{id}/", response_model=VariationOut)
async def update_variation(id: int, payload: VariationUpdate):
    variation = await manager.variation_by(id)
    if not variation:
        raise HTTPException(
            status_code=404,
            detail="Variation not found",
        )

    update_data = payload.dict(exclude_unset=True)

    variation_in_db = VariationIn(**variation)
    updated_variation = variation_in_db.copy(update=update_data)
    return await manager.update(id, updated_variation)


@variationsapi.delete("/{id}/", response_model=None)
async def delete_variation(id: int):
    variation = await manager.variation_by(id)
    if not variation:
        raise HTTPException(status_code=404, detail="Variation not found")
    return await manager.delete(id)
