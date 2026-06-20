from pydantic import BaseModel
from typing import List,Optional
class CourseOut(BaseModel):
    id: int
    title: str
    class Config:
        from_attributes = True # Pydantic v2 (was orm_mode in v1)
class CourseCreate(BaseModel):
    title:str
class UserRegister(BaseModel):
        name: str
        email: str
        password: str
class UserOut(BaseModel):
    id: int
    name: str
    email: str
    courses: List[CourseOut] = [] # nested list of courses
    class Config:
        from_attributes = True
class Token(BaseModel):
        access_token: str
        token_type: str
class TokenData(BaseModel):
        id: Optional[int] = None