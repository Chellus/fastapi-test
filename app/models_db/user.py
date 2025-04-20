from sqlmodel import Field, SQLModel

class Users(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True, index=True)
    name: str
    username: str = Field(default=None, unique=True, index=True)
    email: str = Field(default=None, unique=True)
    password: str
