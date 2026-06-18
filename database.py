'''
    HINTS BY @STUDYHAXER(HAFIZ ATTA UR RAHMAN)
    STEP1:- IMPORT NECCESSARY MODULES AS PER sqlalchmey documentation
    STEP2:- SET DB URL
    STEP3:- SET ENGINE
    STEP4:- SET LOCAL SESSION
    STEP5:- SET BASE
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./user_course.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()