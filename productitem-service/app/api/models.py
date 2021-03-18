from pydantic import BaseModel
from typing import Optional


class ProductItemIn(BaseModel):
    name: str
    image: str
    image_url: str
    product_id: int
    active: bool


class ProductItemOut(ProductItemIn):
    id: int


class ProductItemUpdate(ProductItemIn):
    name: Optional[str] = None
    image: Optional[str] = None
    image_url: Optional[str] = None
    product_id: Optional[int] = None
    active: Optional[bool] = None
