import os

from sqlalchemy import (
    Column,
    create_engine,
    Date,
    Integer,
    MetaData,
    String,
    Table,
)

import timezone
from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

deliveryconfirmations = Table(
    "delivery_confirmation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("expiry", Date, nullable=False, index=True, default=timezone.now),
    Column("code", String(100), nullable=False),
    Column("delivery_id", Integer),
)

database = Database(DATABASE_URI)
