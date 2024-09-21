'''
Ejercicio 6.
Crea un programa que permita al usuario ingresar información de varios estudiantes (nombre, edad, calificación). El programa debe permitir al usuario: 
•	Agregar un nuevo estudiante. 
•	Actualizar estudiantes 
•	Consultar estudiantes 
•	Eliminar estudiante. 
•	Utilizar validaciones y manejo de errores 
•	Debe ser modular el programa
'''


#creaccion lista parta reclamar los estudiantes 
estudiantes = []

# CRUD = C=create R=read U=update D=delete
#funcion para mostrar el menu de opciones
def menu():
    print("/n**** menu de opciones ****")
    print("1. agregar estudiante")
    print("2. actualizar estudiante")
    print("3. eliminar estudiante")
    print("4. lista de todos los estudiante")
    print("5. salir")
    print("/n******************************")


def agregarEstudiante ():
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad <= 0:
                print("La edad debe ser un numero positivo")
                continue
            break
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero para la edad")
    
    while True:
        try: 
            calificacion = float(input(f"Ingrese la calificacion del estudiante {nombre} : "))
            if calificacion < 0 or calificacion > 100:
                print("La calificacion debe estar entre 0  y 100")
                continue
            break
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero para la calificacion")
    
    estudiante = {"nombre": nombre, "edad": edad, "calificacion": calificacion}
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado existosamente ")
    #print(estudiantes) #Para probar cada funcion


def actualizarEstudiante():
    nombre = input("Ingrese el nombre del estudiante a actualizar: ").strip()
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            print(f"Actualizando informacion de {nombre} ")
            estudiante["edad"] = int(input("Ingrese la nueva edad: "))
            estudiante ["calificacion"] = float(input("Ingrese la nueva calificacion: "))
            print(f"informacion de {nombre} actualizada exitosamente")
            #print(estudiantes)#Para probar cada funcion
            return
    print (f"No se encontro ningun estudiante con el nombre {nombre}")


def consultarEstudiante():
    if not estudiantes:
        print("no hay estudiantes registrados")
    else:
        print("\nLista de estudiantes: ")
        for ind, estudiante in enumerate(estudiantes):
            print(f"{ind+1}. nombre: {estudiante['nombre']}, edad: {estudiante['edad']}, calificacion: {estudiante['calificacion']} ")

        #numerate permite insertar sobre una lista y obtener tanto el indice de cada elemento
        #como el elemento en si.
    #forma de imprimir
    #opcion adicional
    # for estudiante in estudiantes:
    # print(f"{estudiante})

def eliminarEstudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip()
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            estudiante.remove(estudiante)
            print(f"Estudiante {nombre} eliminado exitosamente ")
            return
        print(f"no se envontro estudiante con ell nombre {nombre} ")


def principal():
    while True:
        menu()
        opcion = input("Selleccione una opcion [1-5]: ")
        if opcion == "1":
            agregarEstudiante()
        elif opcion == "2":
            agregarEstudiante()
        elif opcion == "3":
            consultarEstudiante()
        elif opcion == "4":
            eliminarEstudiante()
        elif opcion == "5":
            print("Saliendo.....")
            break
        else:
            print("Opcion no valida, por favor seleccione una opcion dell 1 al 5: ")


principal()






#agregarEstudiante ()
#agregarEstudiante ()
#consultarEstudiante()

#print(actualizarEstudiante())



