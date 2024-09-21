"""
De un grupo de N personas a entrevistar se desea determinar cuántas de ellas incumplen la restricción de movilidad conocida como PICO y Cédula
Determinar la cantidad de persona que incumplen con la citada restricción.
"""

# Definir función para verificar el incumplimiento
def incumple_pico_y_cedula(numero_cedula, dia_actual):
    # Asumiendo que la restricción es de 0 a 5 según el último dígito del número de cédula
    # y que el día de la semana es un número entre 0 (lunes) y 6 (domingo)
    ultimo_digito = numero_cedula % 10
    return (dia_actual % 6) != ultimo_digito

# Solicitar el número total de personas
N = int(input("Introduce el número de personas: "))

# Solicitar el día actual (0 para lunes, 6 para domingo)
dia_actual = int(input("Introduce el día actual (0 para lunes, 6 para domingo): "))

# Contador para las personas que incumplen la restricción
incumplen = 0

# Iterar sobre el número de personas
for _ in range(N):
    numero_cedula = int(input("Introduce el número de cédula: "))
    if incumple_pico_y_cedula(numero_cedula, dia_actual):
        incumplen += 1

# Mostrar la cantidad de personas que incumplen la restricción
print(f"Cantidad de personas que incumplen la restricción: {incumplen}")
