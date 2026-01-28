from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)
    create_dt = Column(DateTime, server_default=func.now())
    update_dt = Column(DateTime, onupdate=func.now())