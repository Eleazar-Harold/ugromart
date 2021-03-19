from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OrderAssignmentIn(BaseModel):
    order_id: int
    sale_date: datetime
    fulfilled: bool


class OrderAssignmentOut(OrderAssignmentIn):
    id: int


class OrderAssignmentUpdate(OrderAssignmentIn):
    order_id: Optional[int] = None
    sale_date: Optional[datetime] = None
    fulfilled: Optional[bool] = None
