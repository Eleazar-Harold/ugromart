import os
import timezone

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

orderassignments = Table(
    "order_assignment",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, nullable=False, index=True),
    Column("sale_date", Date, nullable=False, index=True, default=timezone.now),
    Column("fulfilled", Boolean, default=False, nullable=False),
)

database = Database(DATABASE_URI)
