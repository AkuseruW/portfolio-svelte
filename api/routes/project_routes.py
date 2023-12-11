from typing import List
from sqlalchemy.orm import Session
from api.config.database import get_db
from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile, File
import api.config.schemas as schemas
from api.config.models import Projects
from sqlalchemy.orm import joinedload
from api.dependencies.projects_dependencies import (
    add_skill_to_project,
    upload_project_images,
)

router = APIRouter(prefix="/api/projects", tags=["projects"])


@router.get("/", status_code=200, response_model=list[schemas.Projects])
async def get_projects(db: Session = Depends(get_db)):
    return db.query(Projects).all()

@router.get("/{id}")
async def get_project(id: int, db: Session = Depends(get_db)):
    project = db.get(Projects, id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project_with_images = project.__dict__ | {"images": project.images}
    project_with_skills = project_with_images | {"skills": project.skills}
    
    return project_with_skills

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
    
    if not skills or not name or not description or not link or not dateOfCreation or not images:
        raise HTTPException(status_code=400, detail="Missing required field")
    
    project = Projects(
        name=name, description=description, link=link, dateOfCreation=dateOfCreation
    )

    for image in images:
        new_image = await upload_project_images(image, project_id=project.id)
        project.images.append(new_image)

    db.add(project)
    
    for skill in skills:
        await add_skill_to_project(project_id=project.id, skill=skill, db=db)

    db.commit()
    
    return project


@router.patch("/{id}")
async def update_project(
    id: int,
    name: str = Form(...),
    description: str = Form(...),
    link: str = Form(...),
    dateOfCreation: str = Form(...),
    skills: str = Form(...),
    images: List[UploadFile] = File(None),
    db: Session = Depends(get_db),
):
    project = db.get(Projects, id)
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if images:
        for image in images:
            new_image = await upload_project_images(image, project_id=project.id)
            project.images.append(new_image)
            
    project.name = name
    project.description = description
    project.link = link
    project.dateOfCreation = dateOfCreation
    
    for skill in skills:
        await add_skill_to_project(project_id=project.id, skill=skill)

    db.commit()
    db.refresh(project)
    
    return project