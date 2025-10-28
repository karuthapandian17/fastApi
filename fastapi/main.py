from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from models import User, Gender, Role, UserUpdateRequest
from uuid import UUID, uuid4

app = FastAPI()

db: list[User] = [
    User(
        id=uuid4(),
        first_name="karutha",
        last_name="pandian",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Thanga",
        last_name="kali",
        gender=Gender.female,
        roles=[Role.student]
    )
      
]

@app.get("/api/users")
def users():
    return db

@app.post("/api/users")
def addUser(user: User):
    db.append(user)
    return {"id": user.id}

@app.put("/api/users/{user_id}")
def updateUser( user_Update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_Update.first_name is not None:
                user.first_name = user_Update.first_name
                
            if user_Update.last_name is not None:
                user.last_name = user_Update.last_name
            if user_Update.roles is not None:
                user.roles = user_Update.roles    
        return
    raise HTTPException(
        status_code=404, 
        detail=f"User with id: {user_id} does not exist")       

@app.delete("/api/users/{user_id}")
def deleteUser( user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message":"Deleted"}
    raise HTTPException(
        status_code=404, 
        detail=f"User with id: {user_id} does not exist")