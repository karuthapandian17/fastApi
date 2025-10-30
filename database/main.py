from fastapi import FastAPI
from app.database import databaseConfigratiion
from fastapi import HTTPException

app = FastAPI()

databaseConfigratiion.create_database()

def get_db():
    connection = databaseConfigratiion.create_database()
    if connection is None :
        raise HTTPException(status_code=500, detail="mysql connection error")
    try:
        yield connection
    finally:
        if connection and connection.is_connected():
            print("connected sucessfully")  

@app.get("/")
def home():
    return{"msg":"welcome Guys"}              