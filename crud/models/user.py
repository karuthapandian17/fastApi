from sqlalchemy import Table, Column # type: ignore
from sqlalchemy.sql.sqltypes import Integer, String # type: ignore
from config.db import meta

users = Table(
    'users', meta,
    Column('id',Integer, primary_key=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('password',String(255)),
)