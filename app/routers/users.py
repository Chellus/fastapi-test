from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, status
from app.models import users
from app.db.database import get_session
from app.services import users_service, auth_service
from app.utils.security import get_password_hash
from sqlmodel import Session
router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=users.UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: users.UserCreate, session: Session = Depends(get_session)):
    # first we check if there is already a registered user with the received username
    user_exist = users_service.get_user_by_username(user_data.username, session)

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="That username already exists!"
        )
    
    hashed_password = get_password_hash(user_data.password)
    user = users_service.create_user(user_data.name, user_data.username, user_data.email, hashed_password, session)
    return user

@router.post("/test")
async def test_auth(token: Annotated[str, Depends(auth_service.get_current_user)]):
    return {"message": "ola"}