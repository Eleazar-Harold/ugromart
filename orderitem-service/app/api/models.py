from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OrderItemIn(BaseModel):
    order_id: int
    productitem_id: int
    uom_id: int
    amount: float
    quantity: float
    unit_price: float
    order_date: datetime
    fulfilled: bool


class OrderItemOut(OrderItemIn):
    id: int


class OrderItemUpdate(OrderItemIn):
    order_id: Optional[int] = None
    productitem_id: Optional[int] = None
    uom_id: Optional[int] = None
    amount: Optional[float] = None
    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    order_date: Optional[datetime] = None
    fulfilled: Optional[bool] = None
