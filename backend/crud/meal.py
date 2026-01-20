from sqlalchemy.orm import Session
from models.meal import Meal
from schemas.meal import MealCreate

def create_meal(db: Session, meal: MealCreate) :

    ex_user_id = "song@gmail.com"

    db_meal = Meal(
        name=meal.name,
        user_id=ex_user_id
    )

    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

def get_meals(db: Session, skp: int = 0, limit: int=100):

    return db.query(Meal).offset(skp).limit(limit).all()