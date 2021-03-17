from pydantic import BaseModel
from typing import Optional


class OrderItemIn(BaseModel):
    order_id: int
    productitem_id: int
    uom_id: int
    amount: float
    quantity: float
    unit_price: float
    order_date: date
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
    order_date: Optional[date] = None
    fulfilled: Optional[bool] = None
