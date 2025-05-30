from fastapi import FastAPI
from app.db.database import engine
from sqlmodel import SQLModel
from app.models_db import user
from .routers import users, auth
app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(users.router)
app.include_router(auth.router)
@app.get("/")

def check_health():
    return {"message": "App up and running!"}