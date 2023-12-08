from typing import Optional, List
from pydantic import BaseModel

class SignInRequest(BaseModel):
    email: str
    password: str

class Projects(BaseModel):
    name: str
    description: str
    link: str
    
class Create_Experience(BaseModel):
    title: str
    description: str
    startTime: int
    endTime: Optional[int]
    link: Optional[str]   
    
class Experiences(Create_Experience):
    id: int

class Admin_Schema(BaseModel):
    username: str
    email: str
    full_name: str
    about: str
    age: int
    password: str
    
class Skills(BaseModel):
    id: int
    name: str
    icones: str

class Skills_CategoryCreate(BaseModel):
    name: str

class Skills_Category(Skills_CategoryCreate):
    id: int
    skills: List[Skills]