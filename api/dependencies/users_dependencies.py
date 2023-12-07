from fastapi import Depends
from sqlalchemy.orm import Session
from api.config.models import Admin
from api.config.database import get_db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(email: str, password: str, db: Session = Depends(get_db)):
    user_query = db.query(Admin).filter(Admin.email == email).first()
    if not user_query or not verify_password(password, user_query.password):
        return None
    return user_query