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

@router.get("/pacientes/{paciente_id}", response_model=schemas.Paciente)
def read_paciente(paciente_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.get_paciente(db, paciente_id=paciente_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    return db_paciente

@router.get("/pacientes/", response_model=List[schemas.Paciente])
def read_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pacientes = crud.get_pacientes(db, skip=skip, limit=limit)
    return pacientes

@router.post("/pacientes/", response_model=schemas.Paciente)
def create_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    db_paciente = crud.create_paciente(db=db, paciente=paciente)
    return db_paciente

@router.put("/pacientes/{paciente_id}", response_model=schemas.Paciente)
def update_paciente(paciente_id: int, paciente: schemas.Paciente, db: Session = Depends(get_db)):
    db_paciente = crud.update_paciente(db=db, paciente_id=paciente_id, paciente=paciente)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    return db_paciente

@router.delete("/pacientes/{paciente_id}", response_model=schemas.Paciente)
def delete_paciente(paciente_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.delete_paciente(db=db, paciente_id=paciente_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente not found")
    return db_paciente