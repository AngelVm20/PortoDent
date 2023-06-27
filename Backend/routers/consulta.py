from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Consulta
@router.get("/consultas/{consulta_id}", response_model=schemas.Consulta)
def read_consulta(consulta_id: int, db: Session = Depends(get_db)):
    db_consulta = crud.get_consulta(db, consulta_id=consulta_id)
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    return db_consulta

@router.get("/consultas/", response_model=List[schemas.Consulta])
def read_consultas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    consultas = crud.get_consultas(db, skip=skip, limit=limit)
    return consultas

@router.post("/consultas/", response_model=schemas.Consulta)
def create_consulta(consulta: schemas.ConsultaCreate, db: Session = Depends(get_db)):
    db_consulta = crud.create_consulta(db=db, consulta=consulta)
    return db_consulta

@router.put("/consultas/{consulta_id}", response_model=schemas.Consulta)
def update_consulta(consulta_id: int, consulta: schemas.Consulta, db: Session = Depends(get_db)):
    db_consulta = crud.update_consulta(db=db, consulta_id=consulta_id, consulta=consulta)
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    return db_consulta