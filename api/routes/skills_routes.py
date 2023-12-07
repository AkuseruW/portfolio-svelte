from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from api.config.database import get_db
import api.config.schemas as schemas
from api.config.models import Skills
from api.dependencies.uploads import upload_image_to_cloudinary

router = APIRouter(prefix="/api/skills", tags=["skills"])


@router.get("/", status_code=200, response_model=list[schemas.Skills])
async def get_skills(db: Session = Depends(get_db)):
    return db.query(Skills).all()


@router.post("/", status_code=201, response_model=schemas.Skills)
async def create_skill(
    name: str = Form(...), icones: UploadFile = File(...), db: Session = Depends(get_db)
):
    file = await upload_image_to_cloudinary(icones)
    skill = Skills(name=name, icones=file["secure_url"], public_id=file["public_id"])
    db.add(skill)
    db.commit()

    return skill


@router.patch("/{id}")
async def update_skill(
    id: int,
    name: str = Form(...),
    icones: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    pass


@router.delete("/{id}", status_code=200)
async def delete_skill(id: int, db: Session = Depends(get_db)):
    skill = db.get(Skills, id)

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    db.delete(skill)
    db.commit()

    return {"message": "Skill deleted successfully"}
