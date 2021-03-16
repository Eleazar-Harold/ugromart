from typing import List, Optional

from pydantic import BaseModel


class UomIn(BaseModel):
    name: str
    abbreviation: str
    description: str


class UomOut(UomIn):
    id: int


class UomUpdate(UomIn):
    name: Optional[str] = None
    abbreviation: Optional[str] = None
    description: Optional[str] = None
