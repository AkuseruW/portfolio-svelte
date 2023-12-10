from api.config.models import Skills_to_Project
from api.dependencies.uploads import upload_image_to_cloudinary
import api.config.schemas as schemas


async def upload_project_images(image, project_id):
    file = await upload_image_to_cloudinary(image)
    new_image = schemas.Images(
        image=file["secure_url"],
        public_id=file["public_id"],
        project_id=project_id,
    )

    return new_image


async def add_skill_to_project(project_id, skill):
    new_skill = Skills_to_Project(
        skills_id=skill,
        projects_id=project_id,
    )

    return new_skill