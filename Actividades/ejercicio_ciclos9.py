"""Actividad 9.
Crear una solución informática que determine el
valor a pagar por cada cliente de una empresa que 
factura servicio acorde a la siguiente tabla"""

while True:
    cliente = input("porfavor ingrese su nombre: ")
    print("1. servicio 1")
    print("2. servicio 2")
    print("3. servicio 3")
    servicio = input("Que tipo de servicio desea pagar(1,2 o 3): ")
    cantidad = int(input("por favor ingresa la cantidad de servicio: "))

    if servicio == "1":
        Valor_a_pagar = cantidad *100
        print(f"El servicio tipo{servicio}, no tiene descuento el valor es {Valor_a_pagar}")
    elif servicio == "2" :
        if cantidad >= 50:
            descuento = 0.1
            Valor_a_pagar = 1 - (cantidad * 150 * descuento)
            print(f"El servicio tipo{servicio}, no tiene descuento el valor es {Valor_a_pagar}")
        