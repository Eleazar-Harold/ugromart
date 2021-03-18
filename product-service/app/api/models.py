from pydantic import BaseModel
from typing import Optional


class ProductIn(BaseModel):
    name: str
    code: str
    description: str
    vatable: bool


class ProductOut(ProductIn):
    id: int


class ProductUpdate(ProductIn):
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    vatable: Optional[bool] = None
