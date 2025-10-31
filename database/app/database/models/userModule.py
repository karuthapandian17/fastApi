from pydantic import BaseModel

class UserModel(BaseModel):
    username:str
    age:int
    email:str
    id:int