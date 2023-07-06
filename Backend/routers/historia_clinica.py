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

# HistoriaClinica
@router.get("/historias_clinicas/{historia_id}", response_model=schemas.HistoriaClinica)
def read_historia_clinica(historia_id: int, db: Session = Depends(get_db)):
    db_historia = crud.get_historia_clinica(db, historia_id=historia_id)
    if db_historia is None:
        raise HTTPException(status_code=404, detail="Historia Clínica no encontrada")
    return db_historia

@router.get("/historias_clinicas/", response_model=List[schemas.HistoriaClinica])
def read_historias_clinicas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    historias_clinicas = crud.get_historias_clinicas(db, skip=skip, limit=limit)
    return historias_clinicas


@router.post("/historias_clinicas/", response_model=schemas.HistoriaClinica)
def create_historia_clinica(historia: schemas.HistoriaClinicaCreate, db: Session = Depends(get_db)):
    paciente = crud.get_paciente(db, paciente_id=historia.ID_Paciente)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    if paciente.historias_clinicas:
        raise HTTPException(status_code=400, detail="El paciente ya tiene una historia clínica asociada")
    db_historia = crud.create_historia_clinica(db=db, historia=historia, paciente_id=historia.ID_Paciente)
    return db_historia