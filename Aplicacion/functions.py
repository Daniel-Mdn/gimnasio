import numpy as np
import math
from datetime import date
def IMC(peso, estatura):
    estatura=estatura/100
    return round(peso/(estatura*estatura))

def evaluarIMC(imc):
    evaluacion=""
    if imc<18.5:
        evaluacion="Bajo Peso"
    if imc>=18.5 and imc<=24.9:
        evaluacion="Normal"
    if imc>=25:
        evaluacion="Sobrepeso"
    return evaluacion

def porcentajeGrasa(sexo, cintura, cuello, altura, caderas):
    if sexo=="Femenino":
        PG=495/((1.29579-0.35004*(np.log10(cintura+caderas-cuello))+0.22100*(np.log10(altura)))-450)
    else:
        PG=495/(1.0324-0.19077*(np.log10(cintura-cuello))+0.15456*(np.log10(altura)))-450
    return round(PG)

def rutinaConEjercicios(rutinas, datosEjercicio):
    datosRutinas= list()
    for rut in rutinas:
        ejercicioRut=list()
        ejercicioRut.append(rut[0])
        ejercicioRut.append(rut[1])
        for datosRut in datosEjercicio:
            aux= list()
            if rut[0] == datosRut[0]:
                aux= list([datosRut[1], datosRut[2], datosRut[3], datosRut[4], datosRut[5], datosRut[6]])
                ejercicioRut.append(aux)
        datosRutinas.append(ejercicioRut)
    return datosRutinas

def metabolismo_basal(peso, altura, edad, sexo):
    if sexo=="Femenino":
        m_basal=(10*peso) + (6.25*altura) - (5*edad) - 161
    else:
        m_basal=(10*peso)+(6.25*altura)-(5*edad)+5
    return round(m_basal)

def calcular_edad(fecha_nacimiento):
    hoy= date.today()
    return hoy.year-fecha_nacimiento.year

def calcular_calorias(ejercicio):
    calorias_ejercicio=0
    cant_series_totales=0
    for ej in ejercicio:
        cant_series_totales=cant_series_totales + ej[4]
        calorias_ejercicio= calorias_ejercicio + ej[4]*ej[5]
    return round((calorias_ejercicio) + (cant_series_totales*45)*0.1)
