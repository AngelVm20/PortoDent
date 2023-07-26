from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException
from datetime import date,datetime



# Operaciones CRUD para el modelo Paciente
def get_paciente(db: Session, paciente_id: int):
    return db.query(models.Paciente).filter(models.Paciente.ID_Paciente == paciente_id).first()

def get_pacientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Paciente).offset(skip).limit(limit).all()

def create_paciente(db: Session, paciente: schemas.PacienteCreate):
    # Comprobar si ya existe un paciente con esa cédula
    db_paciente = db.query(models.Paciente).filter(models.Paciente.Cedula == paciente.Cedula).first()
    if db_paciente:
        # Si existe, lanzar una excepción
        raise HTTPException(status_code=400, detail="Número de identificación ya registrado")

    db_paciente = models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente


def update_paciente(db: Session, paciente_id: int, paciente: schemas.PacienteBase):
    db_paciente = get_paciente(db, paciente_id)
    if db_paciente is None:
        return None
    for var, value in paciente.dict().items():
        if var != "ID_Paciente" and value is not None:
            setattr(db_paciente, var, value)
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente


def delete_paciente(db: Session, paciente_id: int):
    db_paciente = get_paciente(db, paciente_id)
    if db_paciente:
        # Eliminar todas las historias clínicas relacionadas al paciente
        db_historias = db.query(models.HistoriaClinica).filter(models.HistoriaClinica.ID_Paciente == paciente_id).all()
        for db_historia in db_historias:
            # Eliminar todas las consultas relacionadas a la historia clínica
            db_consultas = db.query(models.Consulta).filter(models.Consulta.ID_HistoriaC == db_historia.ID_HistoriaC).all()
            for db_consulta in db_consultas:
                db.delete(db_consulta)
            db.delete(db_historia)

        db.delete(db_paciente)
        db.commit()
        return db_paciente
    return None


# Operaciones CRUD para el modelo HistoriaClinica
def get_historia_clinica(db: Session, historia_id: int):
    return db.query(models.HistoriaClinica).filter(models.HistoriaClinica.ID_HistoriaC == historia_id).first()

def get_historias_clinicas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.HistoriaClinica).offset(skip).limit(limit).all()

def create_historia_clinica(db: Session, historia: schemas.HistoriaClinicaCreate, paciente_id: int):
     # Generar la fecha de apertura automáticamente
    historia_dict = historia.dict()
    historia_dict["FechaApertura"] = datetime.now().date()

    db_historia = models.HistoriaClinica(**historia_dict)
    db_historia.ID_Paciente = paciente_id
    db.add(db_historia)
    db.commit()
    db.refresh(db_historia)
    return db_historia



# Operaciones CRUD para el modelo Consulta
def get_consulta(db: Session, consulta_id: int):
    return db.query(models.Consulta).filter(models.Consulta.ID_Consulta == consulta_id).first()

def get_consultas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Consulta).offset(skip).limit(limit).all()

def create_consulta(db: Session, consulta: schemas.ConsultaCreate, historia_id: int):
    # Obtener la última sesión para esta historia clínica
    last_session = db.query(models.Consulta.Sesion).filter(models.Consulta.ID_HistoriaC == historia_id).order_by(models.Consulta.Sesion.desc()).first()

    if last_session:
        next_session = last_session.Sesion + 1  # Incrementar el contador de sesión
    else:
        next_session = 1  # Si no hay consultas previas para esta historia, comenzar desde 1

    consulta_dict = consulta.dict()
    consulta_dict["Sesion"] = next_session

    db_consulta = models.Consulta(**consulta_dict)
    db_consulta.ID_HistoriaC = historia_id
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta

def update_consulta(db: Session, consulta_id: int, consulta: schemas.Consulta):
    db_consulta = get_consulta(db, consulta_id)
    if db_consulta is None:
        return None
    for var, value in vars(consulta).items():
        setattr(db_consulta, var, value) if value else None
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta

def get_consultas_by_historia(db: Session, historia_id: int):
    return db.query(models.Consulta).filter(models.Consulta.ID_HistoriaC == historia_id).all()
