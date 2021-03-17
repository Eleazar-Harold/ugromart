from pydantic import BaseModel
from typing import Optional


class OrderAssignmentIn(BaseModel):
    order_id: int
    sale_date: date
    fulfilled: bool


class OrderAssignmentOut(OrderAssignmentIn):
    id: int


class OrderAssignmentUpdate(OrderAssignmentIn):
    order_id: Optional[int] = None
    sale_date: Optional[date] = None
    fulfilled: Optional[bool] = None
