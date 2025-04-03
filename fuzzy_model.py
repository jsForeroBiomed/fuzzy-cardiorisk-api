import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

presion_sistolica = ctrl.Antecedent(np.arange(90, 181, 1), 'presion_sistolica')
colesterol_total = ctrl.Antecedent(np.arange(100, 301, 1), 'colesterol_total')
indice_masa_corporal = ctrl.Antecedent(np.arange(15, 41, 1), 'indice_masa_corporal')
edad = ctrl.Antecedent(np.arange(18, 91, 1), 'edad')
actividad_fisica = ctrl.Antecedent(np.arange(0, 11, 1), 'actividad_fisica')
cigarrillos_por_dia = ctrl.Antecedent(np.arange(0, 31, 1), 'cigarrillos_por_dia')
riesgo_cardiovascular = ctrl.Consequent(np.arange(0, 101, 1), 'riesgo_cardiovascular')

presion_sistolica['baja'] = fuzz.trimf(presion_sistolica.universe, [90, 90, 120])
presion_sistolica['normal'] = fuzz.trimf(presion_sistolica.universe, [110, 120, 130])
presion_sistolica['alta'] = fuzz.trimf(presion_sistolica.universe, [130, 180, 180])

colesterol_total['bajo'] = fuzz.trimf(colesterol_total.universe, [100, 100, 160])
colesterol_total['medio'] = fuzz.trimf(colesterol_total.universe, [150, 200, 250])
colesterol_total['alto'] = fuzz.trimf(colesterol_total.universe, [240, 300, 300])

indice_masa_corporal['bajo'] = fuzz.trimf(indice_masa_corporal.universe, [15, 15, 18.5])
indice_masa_corporal['normal'] = fuzz.trimf(indice_masa_corporal.universe, [18.5, 22, 25])
indice_masa_corporal['alto'] = fuzz.trimf(indice_masa_corporal.universe, [25, 40, 40])

edad['joven'] = fuzz.trimf(edad.universe, [18, 18, 35])
edad['adulto'] = fuzz.trimf(edad.universe, [30, 45, 60])
edad['mayor'] = fuzz.trimf(edad.universe, [55, 90, 90])

actividad_fisica['baja'] = fuzz.trimf(actividad_fisica.universe, [0, 0, 3])
actividad_fisica['media'] = fuzz.trimf(actividad_fisica.universe, [2, 5, 8])
actividad_fisica['alta'] = fuzz.trimf(actividad_fisica.universe, [7, 10, 10])

cigarrillos_por_dia['no'] = fuzz.trimf(cigarrillos_por_dia.universe, [0, 0, 1])
cigarrillos_por_dia['moderado'] = fuzz.trimf(cigarrillos_por_dia.universe, [1, 10, 20])
cigarrillos_por_dia['alto'] = fuzz.trimf(cigarrillos_por_dia.universe, [15, 30, 30])

riesgo_cardiovascular['bajo'] = fuzz.trimf(riesgo_cardiovascular.universe, [0, 0, 40])
riesgo_cardiovascular['medio'] = fuzz.trimf(riesgo_cardiovascular.universe, [30, 50, 70])
riesgo_cardiovascular['alto'] = fuzz.trimf(riesgo_cardiovascular.universe, [60, 100, 100])

reglas = [
    ctrl.Rule(presion_sistolica['alta'] & colesterol_total['alto'] & edad['mayor'], riesgo_cardiovascular['alto']),
    ctrl.Rule(indice_masa_corporal['alto'] & actividad_fisica['baja'], riesgo_cardiovascular['medio']),
    ctrl.Rule(colesterol_total['bajo'] & actividad_fisica['alta'] & edad['joven'], riesgo_cardiovascular['bajo']),
    ctrl.Rule(cigarrillos_por_dia['alto'] & edad['mayor'], riesgo_cardiovascular['alto']),
    ctrl.Rule(presion_sistolica['normal'] & colesterol_total['medio'] & indice_masa_corporal['normal'] & actividad_fisica['media'] & cigarrillos_por_dia['no'], riesgo_cardiovascular['medio']),
    ctrl.Rule(presion_sistolica['baja'] & colesterol_total['bajo'] & actividad_fisica['alta'], riesgo_cardiovascular['bajo']),
    ctrl.Rule(cigarrillos_por_dia['moderado'] & edad['adulto'], riesgo_cardiovascular['medio']),
]

sistema = ctrl.ControlSystem(reglas)
simulador = ctrl.ControlSystemSimulation(sistema)

def predecir(presion_val, colesterol_val, imc_val, edad_val, actividad_val, cigarros_val):
    simulador.input['presion_sistolica'] = presion_val
    simulador.input['colesterol_total'] = colesterol_val
    simulador.input['indice_masa_corporal'] = imc_val
    simulador.input['edad'] = edad_val
    simulador.input['actividad_fisica'] = actividad_val
    simulador.input['cigarrillos_por_dia'] = cigarros_val
    simulador.compute()
    return round(simulador.output['riesgo_cardiovascular'], 2)

