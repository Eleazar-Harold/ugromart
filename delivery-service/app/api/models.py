from pydantic import BaseModel
from typing import List, Optional


class DeliveryIn(BaseModel):
    delivery_no: str
    delivery_date: date
    amount: float
    order_id: int
    delivery_status_id: int
    payments_id: List[int]


class DeliveryOut(DeliveryIn):
    id: int


class DeliveryUpdate(DeliveryIn):
    delivery_no: Optional[str] = None
    delivery_date: Optional[date] = None
    amount: Optional[float] = None
    order_id: Optional[int] = None
    delivery_status_id: Optional[int] = None
    payments_id: Optional[List[int]] = None
