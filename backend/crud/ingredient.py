from sqlalchemy.orm import Session
from models.ingredient import Ingredient
from schemas.ingredient import IngredientCreate, IngredientUpdate


def get_ingredients(db: Session, skp: int = 0, limit: int=100):
    return db.query(Ingredient).offset(skp).limit(limit).all()

def create_ingredient(db: Session, ingredient: IngredientCreate):
    ex_user_id = "03e7709e-801c-4a99-a4b3-f012a28c456d"

    db_ingredient = Ingredient(
        name=ingredient.name,
        user_id=ex_user_id
    )

    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

def update_ingredient(db: Session, ingredient_id: int, ingredient: IngredientUpdate):
    db_ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()

    if db_ingredient:
        db_ingredient.name = ingredient.name
        db.commit()
        db.refresh(db_ingredient)

    return db_ingredient