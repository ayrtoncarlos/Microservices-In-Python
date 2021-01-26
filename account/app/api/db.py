from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database
from decouple import config

DATABASE_URL = config('DATABASE_ACCOUNT_URL')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

accounts = Table(
    'accounts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
)

database = Database(DATABASE_URL)