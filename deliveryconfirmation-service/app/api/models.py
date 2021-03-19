from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DeliveryConfirmationIn(BaseModel):
    delivery_id: int
    code: str
    expiry: datetime


class DeliveryConfirmationOut(DeliveryConfirmationIn):
    id: int


class DeliveryConfirmationUpdate(DeliveryConfirmationIn):
    delivery_id: Optional[int] = None
    code: Optional[str] = None
    expiry: Optional[datetime] = None
