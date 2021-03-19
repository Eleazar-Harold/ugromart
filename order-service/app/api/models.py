from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OrderIn(BaseModel):
    order_no: str
    order_date: datetime
    delivery_date: datetime
    amount: float


class OrderOut(OrderIn):
    id: int


class OrderUpdate(OrderIn):
    order_no: Optional[str] = None
    order_date: Optional[datetime] = None
    delivery_date: Optional[datetime] = None
    amount: Optional[float] = None
