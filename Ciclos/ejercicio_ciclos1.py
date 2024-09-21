"""
Actividad 1:  Ahora vamos a elaborar un algoritmo que pida un número al usuario, 
e imprima todos los números 
pares desde 2 hasta el número pero que termine el proceso si llega al 10.
"""

numero = int(input("Ingrese el numero: "))
incremento = 2

while incremento <= numero:
    print(incremento)
    if incremento ==10:
        break
    incremento +=2
print("Fin del ciclo")
