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
    PiezaDental16_17_55 : Optional[str] = None
    PiezaDental11_21_51 : Optional[str] = None
    PiezaDental26_27_65 : Optional[str] = None
    PiezaDental36_37_75: Optional[str] = None
    PiezaDental31_41_71: Optional[str] = None
    PiezaDental46_47_85 : Optional[str] = None

    Placa16_17_55 : Optional[int] = None
    Placa11_21_51 : Optional[int] = None
    Placa26_27_65 : Optional[int] = None
    Placa36_37_75 : Optional[int] = None
    Placa31_41_71 : Optional[int] = None
    Placa46_47_85 : Optional[int] = None
    
    Calculo16_17_55 : Optional[int] = None
    Calculo11_21_51 : Optional[int] = None
    Calculo26_27_65 : Optional[int] = None
    Calculo36_37_75 : Optional[int] = None
    Calculo31_41_71 : Optional[int] = None
    Calculo46_47_85 : Optional[int] = None
    
    Gingivitis16_17_55 : Optional[int] = None
    Gingivitis11_21_51 : Optional[int] = None
    Gingivitis26_27_65 : Optional[int] = None
    Gingivitis36_37_75 : Optional[int] = None
    Gingivitis31_41_71 : Optional[int] = None
    Gingivitis46_47_85 : Optional[int] = None

    TotalPlaca : Optional[float] = None
    TotalCalculo : Optional[float] = None
    TotalGingivitis : Optional[float] = None


    EnfermedadPerio: Optional[str] = None
    MalOclusion: Optional[str] = None
    Fluorosis: Optional[str] = None
    #8
    IndiceC : Optional[int] = None
    IndiceP : Optional[int] = None 
    IndiceO : Optional[int] = None 
    TotalCPO : Optional[int] = None 
    Indicedc : Optional[int] = None
    Indicede : Optional[int] = None 
    Indicedo : Optional[int] = None
    Totalceo : Optional[int] = None
    #10
    OpcionPlan: Optional[str] = None
    PlanDiagnostico: Optional[str] = None
    #11
    Diagnostico: Optional[str] = None
    Cie : Optional[str] = None
    PreoDef : Optional[str] = None
    FechaProximaConsulta: date
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
