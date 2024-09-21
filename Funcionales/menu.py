"""
Actividad 6 
Terminar el Menú
"""


def menu():
    print('+'*20)
    print('1. Par')
    print('2. Impar')
    print('3. Primo')
    print('4. Factorial')
    print('0. Salir')
    print('+'*20)

def par(numero):
    if numero % 2 == 0:
        print("El numero es par")
    
    else:
        print("El numero no es par")

def Impar (numero):
    if numero % 2 != 0:
        print("El numero es par")
    
    else:
        print("El numero no es par")

def primo(numero):
    
    for i in range(2,numero):
        if numero % i == 0 :
            return  False
    return True

def factorial(numero):
    factorial = 1
    if numero != 0:
        for i in range (1,numero+1):
            factorial *= i
    return factorial

