from fastapi import FastAPI
from app.db.database import engine
from sqlmodel import SQLModel
from app.models_db import user
app = FastAPI()


SQLModel.metadata.create_all(engine)

@app.get("/")
def check_health():
    return {"message": "App up and running!"}