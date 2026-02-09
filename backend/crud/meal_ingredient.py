from sqlalchemy.orm import Session
from models.meal_ingredient import MealIngredient
from schemas.meal_ingredient import MealIngredientCreate

def create_meal_ingredient(db: Session, mealIngredient: MealIngredientCreate) :

    db_meal_ingredient = MealIngredient(
        meal_id=mealIngredient.meal_id,
        ingredient_id=mealIngredient.ingredient_id,
        quantity=mealIngredient.quantity
    )

    db.add(db_meal_ingredient)
    db.commit()
    db.refresh(mealIngredient)
    return db_meal_ingredient