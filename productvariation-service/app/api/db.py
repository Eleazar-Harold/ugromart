import os

from sqlalchemy import (
    Column,
    create_engine,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.orm import relationship

from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

variations = Table(
    "variation",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, nullable=False, index=True),
)

productvariations = Table(
    "product_variation",
    metadata,
    Column("product_id", Integer, nullable=False, index=True),
    Column("variation_id", Integer, ForeignKey("variation.id"), index=True),
)

database = Database(DATABASE_URI)
