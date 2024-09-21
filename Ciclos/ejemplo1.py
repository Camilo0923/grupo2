#Dividir dos numeros donde ell divisor no debe ser 0 ni negativo

dividendo = float(input("Digite el valor del dividendo: "))
divisor = float(input("Digite ell valor del divisor: "))
contIntentos = 0
while divisor <= 0:
    print(f"El divisor no puede ser 0 ni megativo {divisor}")
    if contIntentos == 2:
        print("La cantidad de intentos supero el limite")
        break
    divisor = float(input("Digite el valor del divisor: "))
    contIntentos +=1

if contIntentos <2:
    resultado = dividendo/divisor
    print (f"El resultado de lla division es {resultado:,.1f}")
