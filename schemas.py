from pydantic import BaseModel
from typing import List
class CourseOut(BaseModel):
    id: int
    title: str
    class Config:
        from_attributes = True # Pydantic v2 (was orm_mode in v1)
class UserCreate(BaseModel):
    name:str
    email:str
class CourseCreate(BaseModel):
    title:str
class UserOut(BaseModel):
    id: int
    name: str
    email: str
    courses: List[CourseOut] = [] # nested list of courses
    class Config:
        from_attributes = True