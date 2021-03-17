from pydantic import BaseModel
from typing import Optional


class OrderIn(BaseModel):
    order_no: str
    order_date: date
    delivery_date: date
    amount: float


class OrderOut(OrderIn):
    id: int


class OrderUpdate(OrderIn):
    order_no: Optional[str] = None
    order_date: Optional[date] = None
    delivery_date: Optional[date] = None
    amount: Optional[float] = None
