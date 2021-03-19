import os

from sqlalchemy import (
    Boolean,
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

categories = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, nullable=False, index=True),
    Column("image", String, nullable=True),
    Column("image_url", String, nullable=True, index=True),
    Column("active", Boolean, nullable=False, default=True),
)

productscategories = Table(
    "product_category",
    metadata,
    Column("category_id", Integer, ForeignKey("category.id"), index=True),
    Column("product_id", Integer, nullable=False, index=True),
)

database = Database(DATABASE_URI)
