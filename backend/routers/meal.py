from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas.meal import MealCreate, MealResponse
from crud import meal as crud_meal

router = APIRouter(
    prefix="/meals",
    tags=["Meals"]
)

@router.get("/", response_model=List[MealResponse])
def read_meals(skp: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_meal.get_meals(db=db, skp=skp, limit=limit)

@router.post("/", response_model=MealResponse)
def create_meal(meal: MealCreate, db: Session = Depends(get_db)):
    return crud_meal.create_meal(db=db, meal=meal)