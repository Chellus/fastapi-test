from app.db.database import create_db_and_tables
from sqlmodel import Field, SQLModel

class Users(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True, index=True)
    name: str
    username: str
    email: str
    age: int
    password: str
