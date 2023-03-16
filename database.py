from sqlalchemy import create_engine, Column, Integer, String,Boolean

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Session

Base = declarative_base()

engine = create_engine("postgresql://postgres:1234@localhost/dokon",echo = True)


class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer,primary_key=True, autoincrement=True)
    nomi = Column(String,nullable=False)
    narxi = Column(Integer,nullable=False)




def get_db():
    db= Session()
    try:
        yield db
    finally:
        db.close()