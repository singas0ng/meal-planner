from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas.ingredient import IngredientCreate, IngredientResponse, IngredientUpdate
from crud import ingredient as crud_ingredient

router = APIRouter(
    prefix="/ingredients",
    tags=["Ingredients"]
)

@router.get("/", response_model=List[IngredientResponse])
def read_ingredients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_ingredient.get_ingredients(db=db, skip=skip, limit=limit)

@router.post("/", response_model=IngredientResponse)
def create_ingredient(ingredient: IngredientCreate, db: Session = Depends(get_db)):
    return crud_ingredient.create_ingredient(db=db, ingredient=ingredient)

@router.put("/{ingredient_id}", response_model=IngredientResponse)
def update_ingredient(ingredient_id : int, ingredient: IngredientUpdate, db: Session = Depends(get_db)):
    update_ingredient = crud_ingredient.update_ingredient(db=db, ingredient_id=ingredient_id, ingredient=ingredient)

    if update_ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    return update_ingredient