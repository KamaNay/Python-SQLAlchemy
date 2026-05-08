from sqlalchemy import MetaData, Table, Column, Integer, String

from db import engine

metadata = MetaData()

client_table = Table(
    "client",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("email", String(255), nullable=False),
)

metadata.create_all(engine)
