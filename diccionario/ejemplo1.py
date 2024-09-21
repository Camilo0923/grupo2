#Estructura de diccionario
diccionario ={"nombre":"carlos",
              "edad":22,
              "cursos":["python","metodologia","socioemocionales"]
            }

#aacceder a los ellemantos del diccionario por medio de lla clave
print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["cursos"])

#acceder a los elementos de la lista contenida en ell diccionario
print(diccionario["nombre"][0])
print(diccionario["nombre"][1])
print(diccionario["nombre"][2])

#acceder por medio de la funcion get(clave)
valor = diccionario.get("edad")
print(valor)
