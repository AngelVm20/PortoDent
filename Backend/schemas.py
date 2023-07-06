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
    ID_Paciente: Optional[int]
    class Config:
        orm_mode = True

class HistoriaClinicaBase(BaseModel):
    ID_Paciente: int

class HistoriaClinicaCreate(HistoriaClinicaBase):
    pass

class HistoriaClinica(HistoriaClinicaBase):
    ID_HistoriaC: Optional[int]

    class Config:
        orm_mode = True

class ConsultaBase(BaseModel):
    ID_HistoriaC: Optional[int] = None
    FechaConsulta: date
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
    MotivoC: Optional[str] = None

class ConsultaCreate(ConsultaBase):
    pass

class Consulta(ConsultaBase):
    ID_Consulta: Optional[str]

    class Config:
        orm_mode = True
