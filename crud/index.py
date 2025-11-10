from fastapi import FastAPI, status, HTTPException
from routes.index import user

app = FastAPI()

app.include_router(user)
