from sqlalchemy import Boolean, column, ForeignKey, Integer, String
from database import  Base

class Book(Base):
    __tablename__ = 'Books'

    id = column(Integer,primary_key = True, index = True)
    title = column(String,index = True)
    description = column(String,index = True)
    author = column(String,index = True)
    year = column(String)