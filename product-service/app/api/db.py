import os

from sqlalchemy import (
    Column,
    create_engine,
    Integer,
    MetaData,
    String,
    Table,
    Text,
)

from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

products = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True, index=True),
    Column("code", String, unique=True, index=True),
    Column("description", Text, unique=True, index=True),
    Column("vatable", Boolean, nullable=False, default=False),
)

database = Database(DATABASE_URI)
