import os

from sqlalchemy import (
    Boolean,
    Column,
    create_engine,
    Integer,
    MetaData,
    String,
    Table,
)

from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

productitems = Table(
    "product_item",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, nullable=False),
    Column("product_id", Integer, nullable=False, index=True),
    Column("image", String, nullable=True),
    Column("image_url", String, nullable=True),
    Column("active", Boolean, nullable=False, default=True),
)

database = Database(DATABASE_URI)
