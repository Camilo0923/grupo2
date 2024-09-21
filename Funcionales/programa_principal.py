from menu import * # El asterisco (*) selecciona llals funciones de 1 libreria o archhivo
#El archivo donde tenga mis funciones debe estar llimpio para evitar calculos o errores innecesarios



def principal ():

    while True:
        menu()

        opcion = input("seleccione la opcion deseadadel menu: ")
        if opcion == "1":
            numero = int(input("Por favor digita un numero: "))
            par(numero)

        elif opcion == "2":
            numero = int(input("por favor digita un numero: "))
            Impar(numero)
        elif opcion == "3":
            numero = int(input("Por favor digita un numero: "))
            es_primo = primo(numero)
            if es_primo:
                print(f"El numero {numero} es primo")
            else:
                print(f"El numero {numero} no es primo")
        elif opcion == "4":
            numero = int(input("Por favor digita el numero: "))
            print(factorial(numero))

        elif opcion == "0":
            break

principal()
