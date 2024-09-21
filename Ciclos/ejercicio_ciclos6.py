"""
Actividad 6.

Martha ha diseñado un juego para que reciba un valor y un total de vidas y determine 
si un jugador Gana o Pierde. El número de vidas, determina el total de números que se 
van a utilizar en el cálculo de forma regresiva comenzando desde el valor entregado. 
Se determina el promedio y si ese promedio es divisible por 2, la persona gana sino, pierde.



Por ejemplo, si enviamos el valor = 27 y un total de vidas = 4, 
el juego calcularía el promedio de (27+26+25+24)/4 = 25.5. 25.5 no es 
divisible por 2 así que el juego retornaría "Pierde". Pero si enviáramos el valor = 15  
y el total de vidas = 7, (15+14+13+12+11+10+9)/7 = 12. 12 es divisible por 2 así que el juego 
retornaría "Gana".

Diseña el código para que un jugador que desconoce las reglas envíe el valor y el número 
de vidas y le retorne si Gana o Pierde. 

Pista: El ciclo se ejecutará tantas veces como vidas haya ingresado el jugador.
"""

valor = int(input("Ingrese ell numero a calcular: "))
vidas = int(input("Ingrese la cantidad de vidas: "))

ejecucion = 0
suma = 0

while ejecucion < vidas:

    suma += valor
    resultado = suma/vidas

    valor -= 1
    ejecucion +=1

juego = resultado % 2

if juego == 0:

    print(f"¡¡¡*GANASTE*!!! e RESULTADO ES:{resultado}")

else:
    print(f"¡¡¡*PERDISTE*!!! el RESULTADO ES:{resultado}")