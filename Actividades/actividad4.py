#Hola

"""
Ejercicio 5: 
Una determinada empresa ha decidido ofrecer descuentos a sus clientes de 
acuerdo al día de la semana en el que se realice la compra, 
para lo cual se requiere un algoritmo que dado el día de la semana (en número), 
y el total a pagar sin descuento, calcule el total incluyendo el descuento. El descuento se 
otorga de acuerdo a la siguiente tabla.

Dia	Descuento
1	5%
2	3%
3	10%
4	4%
5	6%
6	2%
7	1%
"""
# :d

print ("1.lunes")
print ("2.martes")
print ("3.miercoles")
print ("4.jueves")
print ("5.viernes")
print ("6.sabado")
print ("7.domingo")

dia = int(input("Ingrese el dia de la semana: "))  #Me perdi 
valor = float(input("Ingrese el valor del producto: "))
descuento = 0

if dia == 1:
    descuento = 0.05
elif dia == 2:
        descuento = 0.03
elif dia == 3:
        descuento = 0.1
elif dia == 4:
        descuento = 0.04
elif dia == 5:
        descuento = 0.06
elif dia == 6:
        descuento = 0.02
elif dia == 7:
        descuento = 0.01
else: 
    
    print ("Dia invalido") #aqui no falta nada?

if descuento >0: 
    valor_a_pagar = valor-(valor*descuento) #Eso se da cuenta ell programa cuando pone ell dia el ususario
    print (f"El valor a pagar es: {valor_a_pagar}")  


#Si señora. Valle. gracias a todos 