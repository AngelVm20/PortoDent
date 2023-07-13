from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
import download_documents as dd
from database import SessionLocal
from fastapi.responses import FileResponse


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
    db_consulta = crud.create_consulta(db=db, consulta=consulta, historia_id=consulta.ID_HistoriaC)
    return db_consulta


@router.put("/consultas/{consulta_id}", response_model=schemas.Consulta)
def update_consulta(consulta_id: int, consulta: schemas.Consulta, db: Session = Depends(get_db)):
    db_consulta = crud.update_consulta(db=db, consulta_id=consulta_id, consulta=consulta)
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    return db_consulta

@router.get("/historias_clinicas/{historia_id}/consultas", response_model=List[schemas.Consulta])
def read_consultas_by_historia(historia_id: int, db: Session = Depends(get_db)):
    consultas = crud.get_consultas_by_historia(db, historia_id=historia_id)
    return consultas



@router.get("/consultas/{consulta_id}/download", response_model=schemas.Consulta)
def download_consulta(consulta_id: int, db: Session = Depends(get_db)):
    db_consulta = crud.get_consulta(db, consulta_id=consulta_id)
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    
    db_paciente = db_consulta.historia_clinica.paciente
    
    filename = dd.consulta_to_xlsx(db_consulta, db_paciente)

    return FileResponse(filename, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=filename)


@router.get("/historia/{historia_id}/download", response_model=schemas.Consulta)
def download_historia(historia_id: int, db: Session = Depends(get_db)):
    historia_clinica = crud.get_historia_clinica(db, historia_id=historia_id)
    if historia_clinica is None:
        raise HTTPException(status_code=404, detail="Historia clinica no encontrada")
    consultas = crud.get_consultas_by_historia(db, historia_id=historia_id)
    if consultas is None:
        raise HTTPException(status_code=404, detail="No hay consultas para esta historia clinica")
    paciente = crud.get_paciente(db, paciente_id=historia_clinica.ID_Paciente)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    filename = dd.historia_to_xlsx(historia_clinica, paciente, db)
    return FileResponse(filename, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')



