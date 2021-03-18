from pydantic import BaseModel
from typing import Optional


class VariationIn(BaseModel):
    name: str


class VariationOut(VariationIn):
    id: int


class VariationUpdate(VariationIn):
    name: Optional[str] = None


class ProductVariationIn(BaseModel):
    variation_id: int
    product_id: int


class ProductVariationOut(ProductVariationIn):
    pass


class ProductVariationUpdate(ProductVariationIn):
    variation_id: Optional[int] = None
    product_id: Optional[int] = None
