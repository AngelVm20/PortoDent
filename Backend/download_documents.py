from sqlalchemy.orm import Session
import crud, schemas
from openpyxl import load_workbook
from datetime import date
from database import SessionLocal
from fastapi import Depends


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def consulta_to_xlsx(consulta: schemas.Consulta, paciente: schemas.Paciente):
    # Cargar la plantilla
    wb = load_workbook('template.xlsx')
    ws = wb.active

    # Suponemos que conoces las celdas exactas donde quieres insertar los datos
    #Esto es con respecto a los datos de cabecera de la historia clinica
    ws['D2'] = paciente.Nombre
    ws['H2'] = paciente.Apellido
    ws['M2'] = paciente.Sexo
    ws['N2'] = calcular_edad(paciente.FechaNacimiento)

    #ws['X1'] = consulta.ID_Consulta
    ws['O2'] = consulta.ID_HistoriaC
    
    #Esto es el campo ciclo de vida del paciente 
    ws['B4'] = consulta.RangoAños

    #Esto ya es con respecto al motico de la consulta
    ws['A7'] = consulta.MotivoC

    #Esto es con respecto al punto 2 enfermedad o problema actual
    ws['A10'] = consulta.EnfActual

    #Esto es con respecto al punto 3 antecedentes personales y familiares
    ws['B13'] = consulta.OpcionesAntecedentes
    ws['A14'] = consulta.Antecedentes

    #Esto es con respecto al punto 4 Signos vitales
    ws['B17'] = consulta.SignosVitales
    ws['F17'] = consulta.FrecuenciaCar
    ws['J17'] = consulta.Temperatura
    ws['O17'] = consulta.FrecuenciaRes

    #Esto es con respecto al punto 5 Examen del sistema estognatico
    ws['C20'] = consulta.OpcionesEstomatognatico
    ws['A21'] = consulta.ExamenEstomat

    #Esto es con respecto al punto 6 Odontograma
    ws['A24'] = consulta.Odontograma

    #Esto es con respecto al punto 7 indicadores de salud bucal
    ws['J48'] = consulta.IndicadoresSalud
    ws['J49'] = consulta.EnfermedadPerio
    ws['J50'] = consulta.MalOclusion
    ws['J51'] = consulta.Fluorosis

    #Esto es con respecto al punto 8 Indices CPO-ceo
    ws['S48'] = consulta.IndicesCPO

    #Esto es con respecto al punto 9 planes de diagnostico, terapeutico y educacional
    ws['D61'] = consulta.OpcionPlan
    ws['A62'] = consulta.PlanDiagnostico

    #Esto es con respecto al punto 11 diagnostico
    ws['A65'] = consulta.Diagnostico

    #Esto es con respecto al punto 12 tratamiento
    ws['D73'] = consulta.Tratamientos
    ws['I73'] = consulta.Procedimientos
    ws['B74'] = consulta.FechaConsulta
    ws['O73'] = consulta.Prescripcion
    ws['V73'] = consulta.Codigo


    # Guardar el archivo temporalmente y retornar su nombre
    filename = f"{paciente.Nombre}{paciente.Apellido}_{paciente.Cedula}_consulta.xlsx"
    wb.save(filename)
    return filename


def historia_to_xlsx(historia: schemas.HistoriaClinica, paciente: schemas.Paciente, db: Session):
    # Cargar la plantilla
    wb = load_workbook('template.xlsx')
    ws = wb.active

    # Datos de cabecera de la historia clinica
    ws['D2'] = paciente.Nombre
    ws['H2'] = paciente.Apellido
    ws['M2'] = paciente.Sexo
    ws['N2'] = calcular_edad(paciente.FechaNacimiento)
    ws['O2'] = historia.ID_HistoriaC

    # Obtener todas las consultas para esta historia clínica
    consultas = crud.get_consultas_by_historia(db, historia.ID_HistoriaC)
    
    for i, consulta in enumerate(consultas):
        # Si esta no es la primera consulta, insertar filas para hacer espacio para los nuevos datos
        if i != 0:
            ws.insert_rows(idx=7, amount=70)  # Ajusta el número de filas según tu plantilla

        # Actualizar el índice para reflejar las filas insertadas
        idx = i * 70  # Ajusta esto según el número de filas que has insertado

        #Esto es el campo ciclo de vida del paciente 
        ws['B4'] = consulta.RangoAños

        #Esto ya es con respecto al punto 1 motivo de la consulta
        ws[f'A{7+idx}'] = consulta.MotivoC

        #Esto es con respecto al punto 2 enfermedad o problema actual
        ws[f'A{10+idx}'] = consulta.EnfActual

        #Esto es con respecto al punto 3 antecedentes personales y familiares
        ws[f'B{13+idx}'] = consulta.OpcionesAntecedentes
        ws[f'A{14+idx}'] = consulta.Antecedentes

        #Esto es con respecto al punto 4 Signos vitales
        ws[f'B{17+idx}'] = consulta.SignosVitales
        ws[f'F{17+idx}'] = consulta.FrecuenciaCar
        ws[f'J{17+idx}'] = consulta.Temperatura
        ws[f'O{17+idx}'] = consulta.FrecuenciaRes

        #Esto es con respecto al punto 5 Examen del sistema estognatico
        ws[f'C{20+idx}'] = consulta.OpcionesEstomatognatico
        ws[f'A{21+idx}'] = consulta.ExamenEstomat

        #Esto es con respecto al punto 6 Odontograma
        ws['A24'] = consulta.Odontograma

        #Esto es con respecto al punto 7 indicadores de salud bucal
        ws[f'J{48+idx}'] = consulta.IndicadoresSalud
        ws[f'J{49+idx}'] = consulta.EnfermedadPerio
        ws[f'J{50+idx}'] = consulta.MalOclusion
        ws[f'J{51+idx}'] = consulta.Fluorosis

        #Esto es con respecto al punto 8 Indices CPO-ceo
        ws[f'S{48+idx}'] = consulta.IndicesCPO

        #Esto es con respecto al punto 10 planes de diagnostico, terapeutico y educacional
        ws[f'D{61+idx}'] = consulta.OpcionPlan
        ws[f'A{62+idx}'] = consulta.PlanDiagnostico

        #Esto es con respecto al punto 11 diagnostico
        ws[f'A{65+idx}'] = consulta.Diagnostico

        #Esto es con respecto al punto 12 tratamiento
        ws[f'D{73+idx}'] = consulta.Tratamientos
        ws[f'I{73+idx}'] = consulta.Procedimientos
        ws[f'B{74+idx}'] = consulta.FechaConsulta
        ws[f'O{73+idx}'] = consulta.Prescripcion
        ws[f'V{73+idx}'] = consulta.Codigo

    # Guardar el archivo y retornar su nombre
    filename = f"{paciente.Nombre}{paciente.Apellido}_{paciente.Cedula}_historia.xlsx"
    wb.save(filename)
    return filename


def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad