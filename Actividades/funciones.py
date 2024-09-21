#sintaxis de la funcion
"""
def nombrefuncion():
    #cuerpo de la funcion
    #codigo que se ejecuta cuando se llama lla funcion

nombrefuncion()

"""

#Funcion sin pparametro ni retorno
def Saludar ():
    print("HHola, bienvenidos a python")


#Saludar()

#Funcion con parametro sin retorno
def sumar(a,b):
    resultado = a+b
    print(f"La suma de {a} y {b} es {resultado} ")

#llamar a la funcion con argumentos o parametros

#se dene respetar los parametros del llamados, si esta en blanco se deja en blanco, si tiene algo se debe porner algo

#llamar a la funcion con argumentos o parametros
#num1 = int(input("ingrese numero1: "))
#num2 = int(input("ingrese numero2: "))
#sumar(num1,num2)

#funcion con retorno de valor
def multiplicar(x,y):
    resultado = x+y
    return resultado

resultadoMul = multiplicar(4,6)
print(resultadoMul+5)




