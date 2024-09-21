"""
Actividad 7.
Crea una aplicación para el siguiente juego. 
    a)  El programa de computador piensa un número
    b)  El concursante cuenta con un máximo de 5 intentos
    c)  Cada vez que el concursante indica un número, el programa le informa si: 
        i)  Gano
        ii) Es mayor que el que pensó
        iii)Es menor que el que pensó
    d)  Si se agotan los turnos sin haber adivinado el número, el programa debe informar el número que había pensado.
"""

#7.leer nombre, edad y estatura de 2 personas, mostrar el nombre y la estatura del mas alto.

nombre1 = input("Ingrese nombre: ")
edad1= int(input("Ingrese edad: "))
estatura1=float(input("Ingrese estatura: "))


nombre2 = input("Ingrese nombre: ")
edad2= int(input("Ingrese edad: "))
estatura2=float(input("Ingrese estatura: "))

if estatura1>estatura2:
    print("la persona mas alta es: ", nombre1, " mide: ", estatura1)
else:
    if estatura1==estatura2 :
        print("Ambas personas miden lo mismo: ", estatura2)
    else:
        print("la persona mas alta es: ", nombre2, " mide: ", estatura2)
