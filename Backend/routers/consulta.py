from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
import download_documents as dd
from database import SessionLocal
from fastapi.responses import StreamingResponse, Response
import os
from urllib.parse import quote




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

@router.get("/consultas/{consulta_id}/download")
async def download_consulta(consulta_id: int, db: Session = Depends(get_db)):
    db_consulta = crud.get_consulta(db, consulta_id=consulta_id)
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    
    db_paciente = db_consulta.historia_clinica.paciente
    
    filename = dd.consulta_to_xlsx(db_consulta, db_paciente)

    def iterfile():  # función generadora
        with open(filename, mode="rb") as file:  # abre el archivo en modo binario
            yield from file  # lee y envía el archivo
        # Se ha movido la eliminación del archivo aquí
        os.remove(filename)  # elimina el archivo una vez que se ha leído completamente

    response = StreamingResponse(iterfile(), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    file_name = quote(filename)  # Esto ayuda a manejar caracteres especiales y espacios en el nombre del archivo
    response.headers["Content-Disposition"] = f"attachment; filename={file_name}"

    return response