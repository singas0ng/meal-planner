from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from database import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)
    created_dt = Column(String, server_default=func.now(), nullable=False)