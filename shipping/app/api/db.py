from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database
from decouple import config

DATABASE_URL = config('DATABASE_SHIPPING_URL')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

shipments = Table(
    'shipments',
    metadata,
    Column('id', Integer, primary_key=True)
)

database = Database(DATABASE_URL)