from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DeliveryItemIn(BaseModel):
    delivery_id: int
    productitem_id: int
    uom_id: int
    amount: float
    quantity: float
    unit_price: float
    delivery_date: datetime


class DeliveryItemOut(DeliveryItemIn):
    id: int


class DeliveryItemUpdate(DeliveryItemIn):
    delivery_id: Optional[int] = None
    productitem_id: Optional[int] = None
    uom_id: Optional[int] = None
    amount: Optional[float] = None
    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    delivery_date: Optional[datetime] = None
