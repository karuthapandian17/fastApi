from fastapi import FastAPI, Body, Depends
from app.database import databaseConfigratiion
from fastapi import HTTPException
from app.database.models.userModule import UserModel

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

@app.post("/createUser", response_model=dict)
async def add_user(user: UserModel = Body(...), connection = Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO user (username, age, email) VALUES (%s,%s,%s)"
            cursor.execute(insert_query, (user.username, user.age, user.email))
            connection.commit()
            print("user created successfully")
            databaseConfigratiion.connectionClose(connection)
            return{"message":"user created"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")   

@app.get('/get', response_model=dict)
async def get_user(connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "SELECT * FROM `user`"
            cursor.execute(insert_query)
            data = cursor.fetchall()
            connection.commit()
            if not data:
                 return {"message":"no user"}

            databaseConfigratiion.connectionClose(connection)
            return{"message": data}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")
    
@app.post('/update', response_model=dict)
async def update_user(user: UserModel = Body(...), connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "UPDATE user SET username =%s , age =%s , email =%s WHERE id =%s"
            cursor.execute(insert_query, (user.username, user.age, user.email, user.id,))
            
            connection.commit()
           

            databaseConfigratiion.connectionClose(connection)
            return{"message": "updated sucessfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")

@app.delete('/delete', response_model=dict)
async def delete_user(user: UserModel = Body(...), connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "DELETE FROM user WHERE id =%s "
            cursor.execute(insert_query, (user.id,))
            
            connection.commit()
           
           

            databaseConfigratiion.connectionClose(connection)
            return{"message": "deleted sucessfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")        
