import matplotlib.pyplot as plt

# Definir variables
ingresos_trabajo_1 = 30000  # Ingresos mensuales por su primer trabajo
ingresos_trabajo_2 = 15000  # Ingresos mensuales por un segundo trabajo
gastos_fijos = 26000  # Gastos mensuales fijos
ingresos_posteriores = 70000  # Ingresos mensuales después de estudiar
meses_estudio = 48  # Duración de los estudios en meses
horizonte = 4*meses_estudio  # Horizonte temporal en meses (10 años)
rendimiento_minimo_mensual = 0.005
patrimonio_inicial = -200000

# Inicializar listas para almacenar los datos del patrimonio para cada escenario
meses_escenario_1 = []
patrimonio_escenario_1 = []
meses_escenario_2 = []
patrimonio_escenario_2 = []

# Calcular el patrimonio para el escenario 1: Estudiando
patrimonio_actual_1 = patrimonio_inicial
for mes in range(horizonte):
    if patrimonio_actual_1>0:
        patrimonio_actual_1 *= (1+rendimiento_minimo_mensual)
    if mes < meses_estudio:
        patrimonio_actual_1 += ingresos_trabajo_1 - gastos_fijos
    else:
        patrimonio_actual_1 += ingresos_posteriores - gastos_fijos
    meses_escenario_1.append(mes)
    patrimonio_escenario_1.append(patrimonio_actual_1)

# Calcular el patrimonio para el escenario 2: Aceptando un segundo trabajo desde el principio
patrimonio_actual_2 = patrimonio_inicial
for mes in range(horizonte):
    if patrimonio_actual_2>0:
        patrimonio_actual_2 *= (1+rendimiento_minimo_mensual)
    patrimonio_actual_2 += ingresos_trabajo_1 + ingresos_trabajo_2 - gastos_fijos
    meses_escenario_2.append(mes)
    patrimonio_escenario_2.append(patrimonio_actual_2)

# Graficar la evolución del patrimonio para ambos escenarios
plt.figure(figsize=(10, 6))
plt.plot(meses_escenario_1, patrimonio_escenario_1, label='Estudiando')
plt.plot(meses_escenario_2, patrimonio_escenario_2, label='Segundo trabajo')
plt.xlabel('Mes')
plt.ylabel('Patrimonio (L.)')
plt.title('Comparación de escenarios')
plt.legend()
plt.grid(True)
plt.show()
