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
    RangoAños: Optional[str] = None
    #1
    MotivoC: Optional[str] = None
    #2
    EnfActual: Optional[str] = None
    #3
    OpcionesAntecedentes: Optional[str] = None
    Antecedentes: Optional[str] = None
    #4
    SignosVitales: Optional[str] = None
    FrecuenciaCar: Optional[str] = None
    Temperatura: Optional[str] = None
    FrecuenciaRes: Optional[str] = None
    #5
    OpcionesEstomatognatico: Optional[str] = None
    ExamenEstomat: Optional[str] = None
    #6
    Odontograma: Optional[str] = None
    #7
    IndicadoresSalud: Optional[str] = None
    EnfermedadPerio: Optional[str] = None
    MalOclusion: Optional[str] = None
    Fluorosis: Optional[str] = None
    #8
    IndicesCPO: Optional[str] = None
    #10
    OpcionPlan: Optional[str] = None
    PlanDiagnostico: Optional[str] = None
    #11
    Diagnostico: Optional[str] = None
    #12
    FechaConsulta: date
    Tratamientos: Optional[str] = None
    Procedimientos: Optional[str] = None
    Prescripcion: Optional[str] = None
    Codigo: Optional[str] = None
    
    
    
    
    
    
    

class ConsultaCreate(ConsultaBase):
    pass

class Consulta(ConsultaBase):
    ID_Consulta: Optional[str]

    class Config:
        orm_mode = True
