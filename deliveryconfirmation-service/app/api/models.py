from pydantic import BaseModel
from typing import Optional


class DeliveryConfirmationIn(BaseModel):
    delivery_id: int
    code: str
    expiry: date


class DeliveryConfirmationOut(DeliveryConfirmationIn):
    id: int


class DeliveryConfirmationUpdate(DeliveryConfirmationIn):
    delivery_id: Optional[int] = None
    code: Optional[str] = None
    expiry: Optional[date] = None
