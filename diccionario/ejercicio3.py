"""
Ejercicio 3.
1.	Crea un programa que permita al usuario ingresar información de varios estudiantes 
(nombre, edad, calificación).
2.	El programa debe permitir al usuario:
o	Agregar un nuevo estudiante.
o	Actualizar la calificación de un estudiante existente.
o	Eliminar a un estudiante.
3.	Finalmente, imprime todos los estudiantes y su información.

"""

#creacion del diccionario vacio
estudiantes = {}

#funcion para mostrar el menu de opcion
def menu():
    print("/n**** menu de opciones ****")
    print("1. agregar estudiante")
    print("2. actualizar estudiante")
    print("3. eliminar estudiante")
    print("4. lista de todos los estudiante")
    print("5. salir")
    print("/n******************************")

#menu()
#Agregar estudiantes

def agregarEst():
    id = int(input("ingrese id del estudiante: "))
    if id in estudiantes:
        print("El id del estudiante ya existe")
    else:
        nombre = input("ingrese nombre del estudiante: ")
        edad = int(input("ingrese edad del estudiante: "))
        calificacion = float(input("Ingrese calificacion del estudiante: "))
        estudiantes[id]={"nombre": nombre, "edad": edad, "calificacio": calificacion}
        
        print(f"estudiante {id} agregado")
        #print(estudiantes)

#agregarEst()




def actualizarCalEst():
    id = int(input("Ingrese el id del estudiante a actualizar: "))
    if id in estudiantes:
        nuevaCalificacion = float(input("ingrese nueva calificacion: "))
        estudiantes [id]["calificacion"]=nuevaCalificacion
        print(f"calificacion del estudiante {id} actualizada ")
        #print(estudiantes)
    else:
        print("El estudiante no existe")



def eliminarEst():
    id = int(input("Ingrese el id del estudiante a eliminar: "))
    if id in estudiantes:
        del estudiantes[id]
        print(f"Estudiante {id} eliminado ")
        #print(estudiantes)
    else:
        print("El estudiante no existe")

def listarEst():
    if estudiantes:
        print("Informacion del estudiantes")
        for clave, valor in estudiantes.items():
            print(f"id: {clave}, nombre: {valor['nombre']}, edad:{valor['edad']}")
    else:
        print("No hay estudiantes registrados")


#agregarEst()
#agregarEst()
#listarEst()
#actualizarCalEst()
#eliminarEst()
 
#programa principal

while True: 
    menu()
    opcion = input("Selecciona una opcion: ")
    if opcion == "1":
        agregarEst()
    elif opcion == "2":
        actualizarCalEst()
    elif opcion == "3":
        eliminarEst()
    elif opcion == "4":
        listarEst()
    elif opcion == "5":
        print ("saliendo.....")
        break
    else:
        print("opcion no valida, seleccione una opcion del menu")

    


