from sqlalchemy.orm import Session
from api.config.database import get_db
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
import api.config.schemas as schemas
from api.config.models import Skills
from api.dependencies.uploads import delete_image, upload_image_to_cloudinary

router = APIRouter(prefix="/api/skills", tags=["skills"])


@router.get("/", status_code=200, response_model=list[schemas.Skills_with_category])
async def get_skills(db: Session = Depends(get_db)):
    skills = db.query(Skills).all()
    skills_with_category = [
        skill.__dict__ | {"category": skill.category.name} for skill in skills
    ]

    return skills_with_category


@router.get("/{id}")
async def get_skill(id: int, db: Session = Depends(get_db)):
    skill = db.get(Skills, id)

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    return skill


@router.post("/", status_code=201, response_model=schemas.Skills)
async def create_skill(
    name: str = Form(...),
    category: int = Form(...),
    icon: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    file = await upload_image_to_cloudinary(icon)
    skill = Skills(
        name=name,
        icones=file["secure_url"],
        category_id=category,
        public_id=file["public_id"],
    )
    db.add(skill)
    db.commit()

    return skill


@router.patch("/{id}")
async def update_skill(
    id: int,
    name: str = Form(...),
    category: int = Form(...),
    icon: UploadFile = File(None),
    db: Session = Depends(get_db),
):
    skill = db.get(Skills, id)

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    if icon:
        print(icon)
        await delete_image(skill.public_id)
        file = await upload_image_to_cloudinary(icon)
        skill.icones = file["secure_url"]
        skill.public_id = file["public_id"]

    skill.name = name
    skill.category_id = category
    
    db.commit()
    db.refresh(skill)

    return skill


@router.delete("/{id}", status_code=200)
async def delete_skill(id: int, db: Session = Depends(get_db)):
    skill = db.get(Skills, id)

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    await delete_image(skill.public_id)
    
    db.delete(skill)
    db.commit()

    return {"message": "Skill deleted successfully"}
