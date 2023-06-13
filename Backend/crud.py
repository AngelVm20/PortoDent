from sqlalchemy.orm import Session

import models, schemas

def get_paciente(db: Session, paciente_id: int):
    return db.query(models.Paciente).filter(models.Paciente.ID_Paciente == paciente_id).first()

def get_pacientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Paciente).offset(skip).limit(limit).all()

def create_paciente(db: Session, paciente: schemas.PacienteCreate):
    db_paciente = models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def update_paciente(db: Session, paciente: schemas.Paciente):
    db_paciente = get_paciente(db, paciente.ID_Paciente)
    if db_paciente is None:
        return None
    for var, value in vars(paciente).items():
        setattr(db_paciente, var, value) if value else None
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def delete_paciente(db: Session, paciente_id: int):
    db_paciente = get_paciente(db, paciente_id)
    if db_paciente is None:
        return None
    db.delete(db_paciente)
    db.commit()
    return db_paciente




# Historia_Clinica CRUD operations
def get_historia_clinica(db: Session, historia_id: int):
    return db.query(models.Historia_Clinica).filter(models.Historia_Clinica.ID_Historia == historia_id).first()

def get_historias_clinicas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Historia_Clinica).offset(skip).limit(limit).all()

def create_historia_clinica(db: Session, historia: schemas.HistoriaClinicaCreate):
    db_historia = models.Historia_Clinica(**historia.dict())
    db.add(db_historia)
    db.commit()
    db.refresh(db_historia)
    return db_historia

# Consulta CRUD operations
def get_consulta(db: Session, consulta_id: int):
    return db.query(models.Consulta).filter(models.Consulta.ID_Consulta == consulta_id).first()

def get_consultas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Consulta).offset(skip).limit(limit).all()

def create_consulta(db: Session, consulta: schemas.ConsultaCreate):
    db_consulta = models.Consulta(**consulta.dict())
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta