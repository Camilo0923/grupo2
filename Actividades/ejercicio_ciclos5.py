"""
Actividad 5.
Escribe un programa usando el ciclo Mientras Que (while) que, dado un número por parte del 
usuario genere la tabla de multiplicar del 1 al 12 para ese número. 
Por ejemplo: Si enviamos el valor=3 el algoritmo devolverá:
3  
6   
9
12  
15  
18  
21  
24  
27  
30  
33  
36  
"""
"""
numero = int(input("Ingrese el numero: "))
i=1

while i<=12:
    multiplicasion= numero*i
    print(f"{numero} x {i}={multiplicasion}")
    i+=1
"""


# Solicitar al usuario que ingrese un número
numero = int(input("Introduce un número: "))

# Inicializar el contador
i = 1

# Mientras el contador sea menor o igual a 12
while i <= 12:
    # Imprimir el resultado de la multiplicación
    print(numero * i)
    # Incrementar el contador
    i += 1
