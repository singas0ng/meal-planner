from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas.meal_ingredient import MealIngredientCreate
from crud import meal_ingredient as crud_meal_ingredient

router = APIRouter(
    prefix="/meal-ingredients",
    tags=["Ingredients"]
)

@router.post("/", response_model=MealIngredientCreate)
def create_meal_ingredient(meal_ingredient: MealIngredientCreate, db: Session = Depends(get_db)):
    return crud_meal_ingredient.create_meal_ingredient(db=db, mealIngredient=meal_ingredient)