"""
Actividad 3:  Usando tanto while como for, escribe el código que pida números al 
usuario hasta que este ingrese -1 y que retorne el factorial de cada número 
ingresado usando un ciclo Para (For).
"""
numero = int(input("por favor ingrese un numero: "))


while numero != -1:
    factorial = 1
    if numero <0:
        print("El factorial no esta definido para los numeros negativos")
    else:
        i =1
        while i <= numero:
            factorial *= i
            i += 1
    print(f"El factorial de {numero} es {factorial}")
    numero = int(input("por favor ingresa un numero: "))