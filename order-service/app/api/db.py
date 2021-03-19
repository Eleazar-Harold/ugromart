import os

from sqlalchemy import (
    Column,
    create_engine,
    Date,
    DECIMAL,
    Integer,
    MetaData,
    String,
    Table,
)

from datetime import datetime
from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

orders = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_date", Date, nullable=False, index=True, default=datetime.now),
    Column("delivery_date", Date, nullable=False, index=True, default=datetime.now),
    Column("order_no", String(50), nullable=False),
    Column("amount", DECIMAL(10, 7), nullable=False),
)

database = Database(DATABASE_URI)
