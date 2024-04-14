import matplotlib.pyplot as plt

# Definir variables comunes
ingresos_anteriores = 8000  # Ingresos mensuales trabajando
gastos_fijos = 7000  # Gastos mensuales fijos
ingresos_posteriores = 20000  # Ingresos mensuales después de estudiar
tasa_interes_anual = 0.18  # Tasa de interés anual del préstamo
meses_estudio = 24  # Duración de los estudios en meses

# Escenario con préstamo educativo
prestamo_mensual = 7000  # Monto del préstamo educativo mensual
cuota_deuda = 10000  # Pago mensual de la deuda al iniciar el trabajo

# Inicializar listas para almacenar los datos de patrimonio
meses = []
patrimonio_con_prestamo = []
patrimonio_sin_prestamo = []

# Calcular el patrimonio mes a mes en ambos escenarios
patrimonio_inicial = 0000 # Patrimonio inicial
rendimiento_ahorros_mes = 0.00
patrimonio_actual_estudiando = patrimonio_inicial
patrimonio_actual_trabajando = patrimonio_inicial
deuda_actual = 0    # Deuda registrada en un determinado banco

# Mientras se está estudiando, o no:
for mes in range(meses_estudio):
    # Escenario con préstamo educativo
    patrimonio_actual_estudiando += deuda_actual   # Se suma para luego restarla actualizada
    patrimonio_actual_estudiando *= (1+rendimiento_ahorros_mes) # El rendimiento del patrimonio si existe
    deuda_actual += prestamo_mensual
    interes_mensual = deuda_actual * (tasa_interes_anual / 12)
    deuda_actual += interes_mensual
    patrimonio_actual_estudiando -= deuda_actual
    meses.append(mes)
    patrimonio_con_prestamo.append(patrimonio_actual_estudiando)
    
    # Escenario sin préstamo educativo
    patrimonio_actual_trabajando += ingresos_anteriores - gastos_fijos
    patrimonio_actual_trabajando *= (1+rendimiento_ahorros_mes) # El rendimiento del patrimonio si existe
    patrimonio_sin_prestamo.append(patrimonio_actual_trabajando)

# Cuando ya se terminó de estudiar, o no:
for mes in range(meses_estudio,5*meses_estudio):
    # Escenario con préstamo educativo
    if deuda_actual>cuota_deuda:
        patrimonio_actual_estudiando += deuda_actual
        patrimonio_actual_estudiando *= (1+rendimiento_ahorros_mes) # El rendimiento del patrimonio si existe
        deuda_actual -= cuota_deuda
        interes_mensual = deuda_actual * (tasa_interes_anual / 12)
        deuda_actual += interes_mensual
        patrimonio_actual_estudiando -= deuda_actual
        meses.append(mes)
        patrimonio_con_prestamo.append(patrimonio_actual_estudiando)
    elif deuda_actual>0:
        patrimonio_actual_estudiando += cuota_deuda
        patrimonio_actual_estudiando *= (1+rendimiento_ahorros_mes) # El rendimiento del patrimonio si existe
        deuda_actual = 0
        print(f'La deuda se terminó de pagar en el mes {mes} avo') 
        meses.append(mes)
        patrimonio_con_prestamo.append(patrimonio_actual_estudiando)
    else:
        patrimonio_actual_estudiando += cuota_deuda
        patrimonio_actual_estudiando *= (1+rendimiento_ahorros_mes) # El rendimiento del patrimonio si existe
        meses.append(mes)
        patrimonio_con_prestamo.append(patrimonio_actual_estudiando)            
  
    # Escenario sin préstamo educativo
    patrimonio_actual_trabajando += ingresos_anteriores - gastos_fijos
    patrimonio_actual_trabajando *= (1+rendimiento_ahorros_mes) # El rendimiento del patrimonio si existe
    patrimonio_sin_prestamo.append(patrimonio_actual_trabajando)

# Graficar la evolución del patrimonio en ambos escenarios
plt.figure(figsize=(10, 6))

plt.plot(meses, patrimonio_con_prestamo, label='Patrimonio al estudiar')
plt.plot(meses, patrimonio_sin_prestamo, label='Patrimonio sin estudiar')

plt.xlabel('Mes')
plt.ylabel('Patrimonio (L.)')
plt.title('Comparación de patrimonio con y sin préstamo educativo')
plt.legend()
plt.grid(True)
plt.show()
