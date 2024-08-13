from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime


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
    historia_clinica = crud.get_historia_clinica(db, historia_id)
    if historia_clinica is None:
        raise HTTPException(status_code=404, detail="Historia clínica no encontrada")
    return historia_clinica

@router.get("/historias_clinicas/", response_model=List[schemas.HistoriaClinica])
def read_historias_clinicas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    historias_clinicas = crud.get_historias_clinicas(db, skip=skip, limit=limit)
    return historias_clinicas

@router.get("/historias_clinicas/paciente/{paciente_id}", response_model=schemas.HistoriaClinica)
def read_historia_clinica_paciente(paciente_id: int, db: Session = Depends(get_db)):
    historia_clinica = crud.get_historias_clinicas(db, paciente_id)
    if historia_clinica is None:
        raise HTTPException(status_code=404, detail="Historia clínica no encontrada")
    return historia_clinica


@router.post("/historias_clinicas/", response_model=schemas.HistoriaClinica)

def create_historia_clinica(historia: schemas.HistoriaClinicaCreate, db: Session = Depends(get_db)):
    paciente = crud.get_paciente(db, paciente_id=historia.ID_Paciente)
    if paciente is None:

        raise HTTPException(status_code=404, detail="Paciente no encontrado en la base de datos")
    if paciente.historias_clinicas:
        raise HTTPException(status_code=400, detail="El paciente ya tiene una historia clínica asociada a su registro")

    # Convertir la fecha a formato ISO y asignarla al campo FechaApertura
    fecha_apertura = datetime.now().isoformat()
    historia_dict = historia.dict()
    historia_dict["FechaApertura"] = fecha_apertura

    db_historia = crud.create_historia_clinica(db=db, historia=schemas.HistoriaClinicaCreate(**historia_dict), paciente_id=historia.ID_Paciente)
    return db_historia
