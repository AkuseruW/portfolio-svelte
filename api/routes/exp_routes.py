from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from api.config.database import get_db
from api.config.models import Experiences
import api.config.schemas as schemas

router = APIRouter(prefix="/api/experiences", tags=["experiences"])


@router.get("/", status_code=200, response_model=list[schemas.Experiences])
async def get_experiences(db: Session = Depends(get_db)):
    return db.query(Experiences).order_by(Experiences.startTime).all()


@router.post("/", status_code=201, response_model=schemas.Create_Experience)
async def create_experience(
    request: schemas.Create_Experience, db: Session = Depends(get_db)
):
    experience = Experiences(
        title=request.title,
        description=request.description,
        startTime=request.startTime,
        endTime=request.endTime,
        link=request.link,
    )
    
    db.add(experience)
    db.commit()
    return experience


@router.patch("/{id}", status_code=200, response_model=schemas.Create_Experience)
async def update_experience(id: int, request: schemas.Create_Experience, db: Session = Depends(get_db)):
    pass


@router.delete("/{id}", status_code=200)
async def delete_experience(id: int, db: Session = Depends(get_db)):
    experience = db.get(Experiences, id)
    
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")
    
    db.delete(experience)
    db.commit()
    
    return {"message": "Experience deleted successfully"}