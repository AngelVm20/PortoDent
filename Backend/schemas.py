from typing import Optional
from pydantic import BaseModel
from datetime import date

class PacienteBase(BaseModel):
    Cedula: str
    Nombre: str
    Apellido: str
    Sexo: str
    FechaNacimiento: date
    Direccion: str
    Telefono: Optional[str] = None
    Email: Optional[str] = None

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    ID_Paciente: int

    class Config:
        orm_mode = True

class HistoriaClinicaBase(BaseModel):
    ID_Paciente: int
    MotivoConsulta: Optional[str] = None
    EnfActual: Optional[str] = None
    Antecedentes: Optional[str] = None
    SignosVitales: Optional[str] = None
    ExamenEstomat: Optional[str] = None
    Odontograma: Optional[str] = None
    IndicadoresSalud: Optional[str] = None
    IndicesCPO: Optional[str] = None
    PlanDiagnostico: Optional[str] = None
    Diagnostico: Optional[str] = None
    Tratamientos: Optional[str] = None

class HistoriaClinicaCreate(HistoriaClinicaBase):
    pass

class HistoriaClinica(HistoriaClinicaBase):
    ID_Historia: int

    class Config:
        orm_mode = True

class ConsultaBase(BaseModel):
    FechaConsulta: date
    ID_Historia: int

class ConsultaCreate(ConsultaBase):
    pass

class Consulta(ConsultaBase):
    ID_Consulta: int

    class Config:
        orm_mode = True
