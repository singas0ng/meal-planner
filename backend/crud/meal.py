from sqlalchemy.orm import Session
from models.meal import Meal
from schemas.meal import MealCreate, MealUpdate


def get_meals(db: Session, skp: int = 0, limit: int=100):
    return db.query(Meal).offset(skp).limit(limit).all()

def create_meal(db: Session, meal: MealCreate) :
    ex_user_id = "03e7709e-801c-4a99-a4b3-f012a28c456d"

    db_meal = Meal(
        name=meal.name,
        user_id=ex_user_id
    )

    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

def update_meal(db: Session, meal_id : int, meal: MealUpdate):
    db_meal = db.query(Meal).filter(Meal.id == meal_id).first()

    if not db_meal:
        return None
    
    db_meal.name = meal.name

    db.commit()
    db.refresh(db_meal)
    return db_meal