from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from database import get_db
from schemas.user import UserCreate, UserResponse, UserUpdate
from crud import user as crud_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=List[UserResponse])
def read_users(skp: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_user.get_users(db=db, skp=skp, limit=limit)

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db=db, user=user)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id : UUID, user: UserUpdate, db: Session = Depends(get_db)):
    update_user = crud_user.update_user(db=db, user_id=user_id, user=user)

    if update_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return update_user