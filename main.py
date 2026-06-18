from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal,engine
from models import User,Course
from typing import List
from schemas import CourseCreate,CourseOut,UserCreate,UserOut
import models
from sqlalchemy.orm import joinedload
from database import Base
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=UserOut)
def create_user(user:UserCreate,db: Session = Depends(get_db)):
    uname = user.name.strip()
    umail = user.email.strip()
    if not uname or not umail:
        raise HTTPException(status_code=422, detail="Name and Email cannot be empty")
    new_user = User(name=uname, email=umail)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/users/{user_id}/courses", response_model=CourseOut)
def create_course_user(user_id:int,course:CourseCreate,db: Session = Depends(get_db)):
    fetchuser = db.query(User).filter(User.id == user_id).first()
    if not fetchuser:
        raise HTTPException(status_code=404, detail="User not found")
    ncourse = course.title.strip()
    if not ncourse:
        raise HTTPException(status_code=422, detail="Course Title cannot be empty")
    new_course = Course(title=ncourse,owner_id = user_id)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course
    
@app.get("/users/{user_id}", response_model=UserOut)
def get_user_details_byid(user_id:int, db: Session = Depends(get_db)):
    fetchuser = db.query(User).options(joinedload(User.courses)).filter(User.id == user_id).first()
    if not fetchuser:
        raise HTTPException(status_code=404, detail="User not found")
    return fetchuser

@app.get("/users", response_model=List[UserOut])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users

@app.delete("/users/{user_id}")
def delete_user_byid(user_id:int, db: Session = Depends(get_db)):
    fetchuser = db.query(User).filter(User.id == user_id).first()
    if not fetchuser:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(fetchuser)
    db.commit()
    return {"message": "User deleted successfully"}