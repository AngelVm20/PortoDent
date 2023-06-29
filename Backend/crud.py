from sqlalchemy.orm import Session
import models, schemas

# Operaciones CRUD para el modelo Paciente
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
    db_historia = models.HistoriaClinica(**historia.dict())
    db_historia.ID_Paciente = paciente_id  # Asignar paciente_id al atributo ID_Paciente
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
    db_consulta = models.Consulta(**consulta.dict())
    db_consulta.ID_HistoriaC=historia_id
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta

def update_consulta(db: Session, consulta: schemas.Consulta):
    db_consulta = get_consulta(db, consulta.ID_Consulta)
    if db_consulta is None:
        return None
    for var, value in vars(consulta).items():
        setattr(db_consulta, var, value) if value else None
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta
