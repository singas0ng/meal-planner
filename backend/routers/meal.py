from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas.meal import MealCreate, MealResponse, MealUpdate
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

@router.put("/{meal_id}", response_model=MealResponse)
def update_meal(meal_id : int, meal: MealUpdate, db: Session = Depends(get_db)):
    update_meal = crud_meal.update_meal(db=db, meal_id=meal_id, meal=meal)
    
    if update_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    
    return update_meal