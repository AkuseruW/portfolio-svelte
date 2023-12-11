from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from api.config.database import get_db
import api.config.schemas as schemas
from api.config.models import Skills_Category

router = APIRouter(prefix="/api/categories", tags=["categories"])


@router.get("/", status_code=200, response_model=list[schemas.Skills_Category])
async def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Skills_Category).all()
    category_with_skills = [
        category.__dict__ | {"skills": category.skills} for category in categories
    ]
    return category_with_skills


@router.get("/{id}")
async def get_category(id: int, db: Session = Depends(get_db)):
    category = db.get(Skills_Category, id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category

@router.post("/", status_code=201, response_model=schemas.Skills_Category)
async def create_category(
    data: schemas.Skills_CategoryCreate, db: Session = Depends(get_db)
):
    category = Skills_Category(name=data.name)
    db.add(category)
    db.commit()

    return category


@router.patch("/{id}")
async def update_category(
    id: int, data: schemas.Skills_CategoryCreate, db: Session = Depends(get_db)
):
    category = db.get(Skills_Category, id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category.name = data.name
    db.commit()
    db.refresh(category)

    return category


@router.delete("/{id}", status_code=200)
async def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.get(Skills_Category, id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()

    return {"message": "Category deleted successfully"}
