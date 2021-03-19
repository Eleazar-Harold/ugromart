import os
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    create_engine,
    Date,
    Integer,
    MetaData,
    Table,
)

from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

orderitems = Table(
    "order_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, nullable=False, index=True),
    Column("productitem_id", Integer, nullable=False, index=True),
    Column("uom_id", Integer, nullable=False, index=True),
    Column("amount", DECIMAL(10, 7), nullable=False),
    Column("quantity", Numeric, nullable=False),
    Column("unit_price", DECIMAL(10, 7), nullable=False),
    Column("order_date", Date, nullable=False, index=True, default=datetime.now),
    Column("fulfilled", Boolean, default=False, nullable=False),
)

database = Database(DATABASE_URI)
