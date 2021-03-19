import os

from databases import Database
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)

from sqlalchemy.ext.declarative import (DeclarativeMeta, declarative_base,)

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
Base: DeclarativeMeta = declarative_base()

class

database = Database(DATABASE_URI)
