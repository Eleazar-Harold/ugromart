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

from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

categories = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, nullable=False),
    Column("image", String, nullable=True),
    Column("image_url", String, nullable=True),
    Column("active", Boolean, nullable=False, default=True),
)

products_categories = Table(
    "product_category",
    metadata,
    Column("category_id", Integer, ForeignKey("category.id")),
    Column("product_id", Integer, nullable=False),
)

database = Database(DATABASE_URI)
