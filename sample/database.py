from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


URL_DATABASE = 'postgresql://postgres:root@localhost:5432/QuizApplicationYT'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind = engine)      
