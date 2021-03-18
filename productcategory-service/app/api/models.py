from pydantic import BaseModel
from typing import Optional


class CategoryIn(BaseModel):
    name: str
    image: str
    image_url: str


class CategoryOut(CategoryIn):
    id: int


class CategoryUpdate(CategoryIn):
    name: Optional[str] = None
    image: Optional[str] = None
    image_url: Optional[str] = None


# class ProductCategoryIn(BaseModel):
#     category_id: int
#     product_id: int


# class ProductCategoryOut(ProductCategoryIn):
#     id: int


# class ProductCategoryUpdate(ProductCategoryIn):
#     category_id: Optional[int] = None
#     product_id: Optional[int] = None
