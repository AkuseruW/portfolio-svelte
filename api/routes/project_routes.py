from typing import List
from sqlalchemy.orm import Session
from api.config.database import get_db
from fastapi import APIRouter, Depends, Form, UploadFile, File
import api.config.schemas as schemas
from api.config.models import Projects
from api.dependencies.projects_dependencies import (
    add_skill_to_project,
    upload_project_images,
)

router = APIRouter(prefix="/api/projects", tags=["projects"])


@router.get("/", status_code=200, response_model=list[schemas.Projects])
async def get_projects(db: Session = Depends(get_db)):
    return db.query(Projects).all()


@router.post("/", status_code=201, response_model=None)
async def create_project(
    name: str = Form(...),
    description: str = Form(...),
    link: str = Form(...),
    dateOfCreation: str = Form(...),
    skills: str = Form(...),
    images: List[UploadFile] = File(...),
    db: Session = Depends(get_db),
):
    project = Projects(
        name=name, description=description, link=link, dateOfCreation=dateOfCreation
    )

    for image in images:
        new_image = await upload_project_images(image, project_id=project.id)
        project.images.append(new_image)

    for skill in skills:
        await add_skill_to_project(project_id=project.id, skill=skill)

    db.add(project)
    db.commit()
    return project
