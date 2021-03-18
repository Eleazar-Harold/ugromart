from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import (
    OrderAssignmentOut,
    OrderAssignmentIn,
    OrderAssignmentUpdate,
)
from app.api import manager
from app.api.service import is_order_present

orderassignmentsapi = APIRouter()


@orderassignmentsapi.post("/", response_model=OrderAssignmentOut, status_code=201)
async def create_assignment(payload: OrderAssignmentIn):
    if not is_order_present(payload.order_id):
        raise HTTPException(
            status_code=404,
            detail=f"Order with given id:{payload.order_id} not found",
        )

    assignment_id = await manager.create(payload)
    response = {"id": assignment_id, **payload.dict()}
    return response


@orderassignmentsapi.get("/", response_model=List[OrderAssignmentOut])
async def get_assignments():
    return await manager.get()


@orderassignmentsapi.get("/{id}/", response_model=OrderAssignmentOut)
async def get_assignment(id: int):
    assignment = await manager.get_by(id)
    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found",
        )
    return assignment


@orderassignmentsapi.put("/{id}/", response_model=OrderAssignmentOut)
async def update_assignment(id: int, payload: OrderAssignmentUpdate):
    assignment = await manager.get_by(id)
    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found",
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

    assignment_in_db = OrderAssignmentIn(**assignment)
    updated_assignment = assignment_in_db.copy(update=update_data)
    return await manager.update(id, updated_assignment)


@orderassignmentsapi.delete("/{id}/", response_model=None)
async def delete_assignment(id: int):
    assignment = await manager.get_by(id)
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return await manager.delete(id)
