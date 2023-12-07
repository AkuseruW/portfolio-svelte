from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from api.config.database import get_db
import api.config.schemas as schemas
from api.config.models import Skills_Category

router = APIRouter(prefix="/api/categories", tags=["categories"])


@router.get("/", status_code=200, response_model=list[schemas.Skills_Category])
async def get_categories(db: Session = Depends(get_db)):
    return db.query(schemas.Skills_Category).all()


@router.post("/", status_code=201, response_model=schemas.Skills_Category)
async def create_category(
    name: schemas.Skills_CategoryCreate, db: Session = Depends(get_db)
):
    category = Skills_Category(name=name)
    db.add(category)
    db.commit()

    return category
