import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import itertools


presion_sistolica = ctrl.Antecedent(np.arange(70, 251, 1), 'presion_sistolica')
colesterol_total = ctrl.Antecedent(np.arange(100, 401, 1), 'colesterol_total')
indice_masa_corporal = ctrl.Antecedent(np.arange(10, 61, 1), 'indice_masa_corporal')
edad = ctrl.Antecedent(np.arange(18, 121, 1), 'edad')
actividad_fisica = ctrl.Antecedent(np.arange(0, 21, 1), 'actividad_fisica') # horas por semana
cigarrillos_por_dia = ctrl.Antecedent(np.arange(0, 60, 1), 'cigarrillos_por_dia')


riesgo_cardiovascular = ctrl.Consequent(np.arange(0, 101, 1), 'riesgo_cardiovascular')


presion_sistolica.automf(names=['baja', 'normal', 'alta'])
colesterol_total.automf(names=['bajo', 'medio', 'alto'])
indice_masa_corporal.automf(names=['bajo', 'normal', 'alto'])
edad.automf(names=['joven', 'adulto', 'mayor'])
actividad_fisica.automf(names=['baja', 'media', 'alta'])
cigarrillos_por_dia.automf(names=['ninguno', 'moderado', 'alto'])


riesgo_cardiovascular['bajo'] = fuzz.trimf(riesgo_cardiovascular.universe, [0, 0, 40])
riesgo_cardiovascular['medio'] = fuzz.trimf(riesgo_cardiovascular.universe, [30, 50, 70])
riesgo_cardiovascular['alto'] = fuzz.trimf(riesgo_cardiovascular.universe, [60, 100, 100])


#valores = {
#    'presion_sistolica': ['baja', 'normal', 'alta'],
#    'colesterol_total': ['bajo', 'medio', 'alto'],
#    'indice_masa_corporal': ['bajo', 'normal', 'alto'],
#    'edad': ['joven', 'adulto', 'mayor'],
#    'actividad_fisica': ['alta', 'media', 'baja'],  # inverso
#    'cigarrillos_por_dia': ['ninguno', 'moderado', 'alto']
#}

valores = {
    'presion_sistolica': ['baja', 'alta'],
    'colesterol_total': ['bajo', 'alto'],
    'indice_masa_corporal': ['bajo', 'alto'],
    'edad': ['joven', 'mayor'],
    'actividad_fisica': ['baja', 'alta'],
    'cigarrillos_por_dia': ['ninguno', 'alto']
}


peso = {
    'baja': 0, 'bajo': 0, 'joven': 0, 'alta': 0, 'ninguno': 0,
    'normal': 1, 'medio': 1, 'adulto': 1, 'media': 1, 'moderado': 1,
    'alta': 2, 'alto': 2, 'mayor': 2, 'baja': 2
}


obj_entrada = [
    presion_sistolica,
    colesterol_total,
    indice_masa_corporal,
    edad,
    actividad_fisica,
    cigarrillos_por_dia
]

reglas = []

print("Generando reglas...")
for combinacion in itertools.product(*valores.values()):
    puntaje = sum(peso[v] for v in combinacion)
    if puntaje <= 5:
        riesgo = riesgo_cardiovascular['bajo']
    elif puntaje <= 9:
        riesgo = riesgo_cardiovascular['medio']
    else:
        riesgo = riesgo_cardiovascular['alto']

    condiciones = [
        obj_entrada[i][valor]
        for i, valor in enumerate(combinacion)
    ]

    regla = ctrl.Rule(condiciones[0] & condiciones[1] & condiciones[2] &
                      condiciones[3] & condiciones[4] & condiciones[5], riesgo)
    reglas.append(regla)


print("Reglas generadas: ", len(reglas))
print("Construyendo sistema difuso")

sistema = ctrl.ControlSystem(reglas)
print("Sistema construido")

print("Instanciando simulador...")
simulador = ctrl.ControlSystemSimulation(sistema)
print("Simulador listo")



def predecir(presion_val, colesterol_val, imc_val, edad_val, actividad_val, cigarros_val):
    try:
        simulador.input['presion_sistolica'] = presion_val
        simulador.input['colesterol_total'] = colesterol_val
        simulador.input['indice_masa_corporal'] = imc_val
        simulador.input['edad'] = edad_val
        simulador.input['actividad_fisica'] = actividad_val
        simulador.input['cigarrillos_por_dia'] = cigarros_val

        simulador.compute()
        return round(simulador.output['riesgo_cardiovascular'], 2)
    except Exception:
        return "No se pudo calcular el riesgo. Intenta con valores dentro del rango."
