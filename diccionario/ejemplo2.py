estudiante = {"nombre":"juan",
              "edad": 24,
              "carrera":"ingenieria",
              "promedio":8.5
              }

#acceder a valores del diccionario
nombreEst = estudiante["nombre"]
print(nombreEst)

edadEst = estudiante.get("edad")
print(edadEst)

#(print(estudiante..get("carrera")))
#modificar valores en el diccionario
estudiante["Edad"]=25

print(estudiante)

#agregar un nuevo para clave - valor
estudiante["graduado"] = False

print(estudiante)

#eliminar un par clave - valor con del
del estudiante["promedio"]
print(estudiante)


#eliminar usando funcion pop()
#estudiante.pop("graduado")
#print(estudiante)

#recorrer la clave del diccionario
#["nombre": "juan", "edad" : 25, "carrera": "ingenieria", "promedio": 8.5, "graduado" ]
for valor in estudiante.values():#valor=25
    print(valor)

#Recorrer la valores del diccionario
#["nombre": "juan", "edad" : 25, "carrera": "ingenieria", "promedio": 8.5, "graduado" ]
for valor in estudiante.values():#valor=25
    print(valor)

#Recorrer tanto cllaves como valores
for clave, valor in estudiante.items():
    print(f"{clave} {valor}")