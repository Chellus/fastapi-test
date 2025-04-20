from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    user_id: int