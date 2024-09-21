# Diseñar un programa que callcule e promedio de notas del rimer 
# parcia de im cuso de N estudiantes

try:
    nEsT = int(input("Digite la cantidad de estudiantes : "))
    sumaNota = 0
    i = 1
    while i <= nEsT:
        nota = float(input(f"Dogite nota de estudiante {i} "))
        sumaNota+=nota
        i+=1

    promedio = sumaNota/nEsT
    print(f"El promedio dell curso es {promedio:,.2f}")
except ValueError:
    print("Error, entradas no pueden ser texto sino numericas")



#try - except < trata de hacer algo o si no sacame de alli. tratamiento de errores del sistema como tal.