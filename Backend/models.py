from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paciente(Base):
    __tablename__ = "Paciente"

    ID_Paciente = Column(Integer, primary_key=True, index=True)
    Cedula = Column(VARCHAR(20), index=True)
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

    paciente = relationship("Paciente", back_populates="historias_clinicas")
    consultas = relationship("Consulta", back_populates="historia_clinica")

class Consulta(Base):
    __tablename__ = "Consulta"

    ID_Consulta = Column(Integer, primary_key=True, index=True)
    ID_HistoriaC = Column(Integer, ForeignKey("HistoriaClinica.ID_HistoriaC"))
    FechaConsulta = Column(Date)
    EnfActual = Column(VARCHAR(200))
    Antecedentes = Column(VARCHAR(200))
    SignosVitales = Column(VARCHAR(200))
    ExamenEstomat = Column(VARCHAR(200))
    Odontograma = Column(VARCHAR(200))
    IndicadoresSalud = Column(VARCHAR(200))
    IndicesCPO = Column(VARCHAR(200))
    PlanDiagnostico = Column(VARCHAR(200))
    Diagnostico = Column(VARCHAR(200))
    Tratamientos = Column(VARCHAR(200))
    MotivoC = Column(VARCHAR(200))

    historia_clinica = relationship("HistoriaClinica", back_populates="consultas")
