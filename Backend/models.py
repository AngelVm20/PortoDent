from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paciente(Base):
    __tablename__ = "Paciente"

    ID_Paciente = Column(Integer, primary_key=True, index=True)
    Cedula = Column(VARCHAR(20), unique=True, index=True)
    Nombre = Column(VARCHAR(50))
    Apellido = Column(VARCHAR(50))
    Sexo = Column(VARCHAR(10))
    FechaNacimiento = Column(Date)
    Direccion = Column(VARCHAR(100))
    Telefono = Column(VARCHAR(20))
    Email = Column(VARCHAR(100))

    historias_clinicas = relationship("HistoriaClinica", back_populates="paciente")

class HistoriaClinica(Base):
    __tablename__ = "HistoriaClinica"

    ID_HistoriaC = Column(Integer, primary_key=True, index=True)
    ID_Paciente = Column(Integer, ForeignKey("Paciente.ID_Paciente"))
    FechaApertura  = Column(Date)

    paciente = relationship("Paciente", back_populates="historias_clinicas")
    consultas = relationship("Consulta", back_populates="historia_clinica")

class Consulta(Base):
    __tablename__ = "Consulta"

    ID_Consulta = Column(Integer, primary_key=True, index=True)
    ID_HistoriaC = Column(Integer, ForeignKey("HistoriaClinica.ID_HistoriaC"))
    RangoAños = Column(VARCHAR(200))
    MotivoC = Column(VARCHAR(200))
    EnfActual = Column(VARCHAR(200))
    OpcionesAntecedentes = Column(VARCHAR(200))
    Antecedentes = Column(VARCHAR(200))
    SignosVitales = Column(VARCHAR(200))
    FrecuenciaCar= Column(VARCHAR(200))
    Temperatura= Column(VARCHAR(200))
    FrecuenciaRes= Column(VARCHAR(200))
    OpcionesEstomatognatico= Column(VARCHAR(200))
    ExamenEstomat = Column(VARCHAR(200))
    Odontograma = Column(VARCHAR(200))

    PiezaDental16_17_55 = Column(VARCHAR(200))
    PiezaDental11_21_51 = Column(VARCHAR(200))
    PiezaDental26_27_65 = Column(VARCHAR(200))
    PiezaDental36_37_75 = Column(VARCHAR(200))
    PiezaDental31_41_71 = Column(VARCHAR(200))
    PiezaDental46_47_85 = Column(VARCHAR(200))

    Placa16_17_55 = Column(Integer)
    Placa11_21_51 = Column(Integer)
    Placa26_27_65 = Column(Integer)
    Placa36_37_75 = Column(Integer)
    Placa31_41_71 = Column(Integer)
    Placa46_47_85 = Column(Integer)

    Calculo16_17_55 = Column(Integer)
    Calculo11_21_51 = Column(Integer)
    Calculo26_27_65 = Column(Integer)
    Calculo36_37_75 = Column(Integer)
    Calculo31_41_71 = Column(Integer)
    Calculo46_47_85 = Column(Integer)
    
    Gingivitis16_17_55 = Column(Integer)
    Gingivitis11_21_51 = Column(Integer)
    Gingivitis26_27_65 = Column(Integer)
    Gingivitis36_37_75 = Column(Integer)
    Gingivitis31_41_71 = Column(Integer)
    Gingivitis46_47_85 = Column(Integer)

    TotalPlaca = Column(Float)
    TotalCalculo = Column(Float) 
    TotalGingivitis = Column(Float) 

    EnfermedadPerio= Column(VARCHAR(200))
    MalOclusion= Column(VARCHAR(200))
    Fluorosis= Column(VARCHAR(200))

    IndiceC = Column(Integer) 
    IndiceP = Column(Integer)
    IndiceO = Column(Integer)
    TotalCPO = Column(Integer) 
    Indicedc = Column(Integer) 
    Indicede = Column(Integer) 
    Indicedo = Column(Integer)
    Totalceo = Column(Integer)

    OpcionPlan = Column(VARCHAR(200))
    PlanDiagnostico = Column(VARCHAR(200))

    Diagnostico = Column(VARCHAR(200))
    Cie = Column(VARCHAR(200))
    PreoDef = Column(VARCHAR(200))
    FechaProximaConsulta = Column(Date)


    FechaConsulta = Column(Date)
    Tratamientos = Column(VARCHAR(200))
    Procedimientos= Column(VARCHAR(200))
    Prescripcion= Column(VARCHAR(200))
    Codigo= Column(VARCHAR(200))
    Sesion = Column(Integer, default=1)

    historia_clinica = relationship("HistoriaClinica", back_populates="consultas")
