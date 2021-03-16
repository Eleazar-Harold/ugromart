import os

import timezone
from databases import Database
from sqlalchemy import (
    ARRAY,
    Column,
    Date,
    DateTime,
    Decimal,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

unitofmeasures = Table(
    "uom",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), unique=True, nullable=False),
    Column("abbreviation", String(50), nullable=False),
    Column("description", String(200), nullable=True),
)

database = Database(DATABASE_URI)
