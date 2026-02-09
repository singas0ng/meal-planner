from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class MealIngredient(Base):
    __tablename__ = "meal_ingredients"

    id = Column(Integer, primary_key=True, index=True)

    #Foreign Keys
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)

    quantity = Column(String, nullable=False) # e.g. "200g", "1 piece"
    create_dt = Column(DateTime, server_default=func.now())
    update_dt = Column(DateTime, onupdate=func.now())