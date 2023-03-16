from fastapi import FastAPI, Depends
from pydantic import BaseModel
from starlette import status, schemas

import database
from database import Product, engine, get_db

app = FastAPI()
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class AdminProduct(BaseModel):

    nomi:str
    narxi:int


@app.get('/')
def home():
    data = session.query(Product).all()
    return {"data":data}


@app.get('/one/{id}')
def homed(id:str):
    data = session.query(Product).filter(Product.nomi==id).all()

    return {"data":data}



@app.post('/add',)
def home(malumot:AdminProduct,):

    c1 = Product(nomi=malumot.nomi,narxi =malumot.narxi)

    session.add(c1)
    session.commit()
    return {"data":malumot.dict()}


@app.delete('/del/{id}')
def homed(id:int):
    data = session.query(Product).filter(Product.id==id).first()
    session.delete(data)
    session.commit()

    return {"data":"Malumot o'childi"}



@app.patch('/{noteId}')
def update_note(noteId: str, payload:AdminProduct ):
    note_query = session.query(Product).filter(Product.id == noteId)
    db_note = note_query.first()


    update_data = payload.dict(exclude_unset=True)
    note_query.filter(Product.id == noteId).update(update_data,
                                                       synchronize_session=False)
    session.commit()
    session.refresh(db_note)
    return {"status": "success", "note": db_note}