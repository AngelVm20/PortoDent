from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

router = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/historias/{historia_id}", response_model=schemas.HistoriaClinica)
def read_historia(historia_id: int, db: Session = Depends(get_db)):
    db_historia = crud.get_historia_clinica(db, historia_id=historia_id)
    if db_historia is None:
        raise HTTPException(status_code=404, detail="Historia not found")
    return db_historia

@router.get("/historias/", response_model=List[schemas.HistoriaClinica])
def read_historias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    historias = crud.get_historias_clinicas(db, skip=skip, limit=limit)
    return historias

@router.post("/historias/", response_model=schemas.HistoriaClinica)
def create_historia(historia: schemas.HistoriaClinicaCreate, db: Session = Depends(get_db)):
    db_historia = crud.create_historia_clinica(db=db, historia=historia)
    return db_historia
