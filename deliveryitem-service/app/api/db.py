import os

from sqlalchemy import (
    Column,
    create_engine,
    Date,
    Decimal,
    Integer,
    MetaData,
    Table,
)

import timezone
from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

deliveryitems = Table(
    "delivery_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("delivery_date", Date, nullable=False, index=True, default=timezone.now),
    Column("amount", Decimal(10, 7), nullable=False),
    Column("quantity", Decimal(10, 7), nullable=False),
    Column("unit_price", Decimal(10, 7), nullable=False),
    Column("productitem_id", Integer),
    Column("uom_id", Integer),
    Column("delivery_id", Integer),
)

database = Database(DATABASE_URI)
