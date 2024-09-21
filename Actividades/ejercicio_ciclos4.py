"""
Actividad 4: Genera un código que, dado un número, calcule la suma de los 
números pares menores al valor hasta el 0. El número se incluye en la suma sea o no par.
Ejemplo: Si el usuario ingresa 21 21+20+18+16+14+12+10+8+6+4+2 = 131
Si el usuario ingresa 6 6+4+2 = 12
"""
#range son par numeros.
numero = int(input("ingrese un numero: "))
suma = numero

for pares in range(2,numero,2):
    suma += pares
print(f"La suma de los numeros pares es de {suma}")
