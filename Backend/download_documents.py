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

    #HIGIENE ORAL SIMPLIFICADA 
    #PIEZAS DENTALES
    ws['C50'] = consulta.PiezaDental16_17_55
    ws['C51'] = consulta.PiezaDental11_21_51
    ws['C52'] = consulta.PiezaDental26_27_65
    ws['C54'] = consulta.PiezaDental36_37_75
    ws['C55'] = consulta.PiezaDental31_41_71
    ws['C56'] = consulta.PiezaDental46_47_85


    #PLACA 
    ws['D50'] = consulta.Placa16_17_55
    ws['D51'] = consulta.Placa11_21_51
    ws['D52'] = consulta.Placa26_27_65
    ws['D54'] = consulta.Placa36_37_75
    ws['D55'] = consulta.Placa31_41_71
    ws['D56'] = consulta.Placa46_47_85
    ws['D57'] = consulta.TotalPlaca

    #CALCULO
    ws['F50'] = consulta.Calculo16_17_55
    ws['F51'] = consulta.Calculo11_21_51
    ws['F52'] = consulta.Calculo26_27_65
    ws['F54'] = consulta.Calculo36_37_75
    ws['F55'] = consulta.Calculo31_41_71
    ws['F56'] = consulta.Calculo46_47_85
    ws['F57'] = consulta.TotalCalculo


    #GINGIVITIS
    ws['H50'] = consulta.Gingivitis16_17_55
    ws['H51'] = consulta.Gingivitis11_21_51
    ws['H52'] = consulta.Gingivitis26_27_65
    ws['H54'] = consulta.Gingivitis36_37_75
    ws['H55'] = consulta.Gingivitis31_41_71
    ws['H56'] = consulta.Gingivitis46_47_85
    ws['H57'] = consulta.TotalGingivitis

    #ENF. PERIODONTAL
    ws['M49'] = consulta.EnfermedadPerio

    #MAL OCLUSION
    ws['O49'] = consulta.MalOclusion

    #FLUOROSIS
    ws['Q49'] = consulta.Fluorosis



    #Esto es con respecto al punto 8 Indices CPO-ceo
    #Indice D
    ws['T49'] = consulta.IndiceC
    ws['U49'] = consulta.IndiceP
    ws['V49'] = consulta.IndiceO
    ws['W49'] = consulta.TotalCPO

    #Indice d
    ws['T51'] = consulta.Indicedc
    ws['U51'] = consulta.Indicede
    ws['V51'] = consulta.Indicedo
    ws['W51'] = consulta.Totalceo

    #Esto es con respecto al punto 10 planes de diagnostico, terapeutico y educacional
    ws['D60'] = consulta.OpcionPlan
    ws['A61'] = consulta.PlanDiagnostico

    #Esto es con respecto al punto 11 diagnostico
    ws['B64'] = consulta.Diagnostico
    ws['M64'] = consulta.Cie
    ws['P64'] = consulta.PreoDef
    ws['F66'] = consulta.FechaProximaConsulta

    #Esto es con respecto al punto 12 tratamiento
    ws['D70'] = consulta.Tratamientos
    ws['I70'] = consulta.Procedimientos
    ws['B71'] = consulta.FechaConsulta
    ws['O70'] = consulta.Prescripcion
    ws['V70'] = consulta.Codigo

    # Guardar el archivo temporalmente y retornar su nombre
    filename = f"{paciente.Nombre}{paciente.Apellido}_{paciente.Cedula}_{consulta.FechaConsulta}_consulta.xlsx"
    wb.save(filename)
    return filename


def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad