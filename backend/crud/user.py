from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext
from uuid import UUID

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):

    hash_password = pwd_context.hash(user.password)

    db_user = User(
        email=user.email,
        password=hash_password,
        nickname=user.nickname,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: UUID, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user:
        # Only update if the value is NOT None
        if user.nickname is not None:
            db_user.nickname = user.nickname
        
        if user.is_active is not None:
            db_user.is_active = user.is_active

        db.commit()
        db.refresh(db_user)

    return db_user