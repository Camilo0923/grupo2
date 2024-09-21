#Escribe un programa que reciba una pallabra y diga cuantas letras
#"a" posee y muestre por pantalla el numero de veces que aparece la letra
#en la palabra

palabra = input("Ingrese una palabra: ").lower() # El programa reconoce por aparte la mayuscula y la minuscula (las cuenta diferentes)
#.lower:  es una funcion que convierte las letras en minusculas
contL = 0
for letra in palabra:
    if letra == "a":
        contL+=1
print(f"La cantidad de letras 'a' que tiene la palabra {palabra} es {contL} ")

#utilizando lla funcion coun()
print (palabra.count('a'))# otra opcion de usar lla variable

