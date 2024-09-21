"""
Actividad 2:  Escribe el código un ciclo para obtener el 
número de dígitos de un número ingresado por el usuario, pero saltarse si el digito es 4.


numero =abs( int(input("Digite un numero: ")))
digitos = 0

while numero > 0:
    if numero %10 == 4 or numero %10 == 5:
        numero = numero//10 
        continue #con esta oppcion de devuelve al inicio del ciclo. 
                 #"significa que no sigue con a operacion del cogigo, si no que se devueve"
    digitos +=1 
    numero = numero//10 

print(f"La cantidad de digitos es {digitos}")

#abs es para poner valores absolutos
"""

numero = input("Digite un numero: ")
cantidadDigitos = 0

for digito in numero:
    if digito == '4':
        continue
cantidadDigitos += 1
print(f"la cantidad de digitos es {cantidadDigitos}")