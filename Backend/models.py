from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base

class Paciente(Base):
    __tablename__ = "Paciente"

    ID_Paciente = Column(Integer, primary_key=True, index=True)
    Cedula = Column(String(20), nullable=False)
    Nombre = Column(String(50), nullable=False)
    Apellido = Column(String(50), nullable=False)
    Sexo = Column(String(1), nullable=False)
    FechaNacimiento = Column(Date, nullable=False)
    Direccion = Column(String(100), nullable=False)
    Telefono = Column(String(20), nullable=True)
    Email = Column(String(100), nullable=True)
    historia_clinica = relationship("Historia_Clinica", back_populates="paciente")


class Historia_Clinica(Base):
    __tablename__ = "Historia_Clinica"

    ID_Historia = Column(Integer, primary_key=True, index=True)
    ID_Paciente = Column(Integer, ForeignKey("Paciente.ID_Paciente"))
    MotivoConsulta = Column(String, nullable=True)
    EnfActual = Column(String, nullable=True)
    Antecedentes = Column(String, nullable=True)
    SignosVitales = Column(String, nullable=True)
    ExamenEstomat = Column(String, nullable=True)
    Odontograma = Column(String, nullable=True)
    IndicadoresSalud = Column(String, nullable=True)
    IndicesCPO = Column(String, nullable=True)
    PlanDiagnostico = Column(String, nullable=True)
    Diagnostico = Column(String, nullable=True)
    Tratamientos = Column(String, nullable=True)
    
    paciente = relationship("Paciente", back_populates="historia_clinica")
    consulta = relationship("Consulta", back_populates="historia_clinica")

class Consulta(Base):
    __tablename__ = "Consulta"

    ID_Consulta = Column(Integer, primary_key=True, index=True)
    FechaConsulta = Column(Date, nullable=False)
    ID_Historia = Column(Integer, ForeignKey("Historia_Clinica.ID_Historia"))
    
    historia_clinica = relationship("Historia_Clinica", back_populates="consulta")