clientes = [] 
paquetes = []
reservas = []

menu = {
    "1": "Registrar cliente",
    "2": "Crear paquete de viaje",
    "3": "Realizar reserva",
    "4": "Cancelar reserva",
    "5": "Mostrar reservas",
    "6": "Mostrar reservas de un cliente",
    "7": "Mostrar clientes",
    "8": "Mostrar paquetes",
    "9": "Eliminar paquete",
    "10": "Eliminar cliente",  
    "11": "Modificar paquete",
    "12": "Mostrar todos los paquetes de todos los clientes", 
    "0": "Salir"
}

# Paquetes de viaje predeterminados
paquetes_preset = [
    {
        "nombre": "Paquete Playa",
        "descripcion": "Vacaciones en la playa con todo incluido.",
        "fecha_salida": "01-12-2023",
        "fecha_llegada": "10-12-2023",
        "precio": 500.00
    },
    {
        "nombre": "Paquete Aventura",
        "descripcion": "Excursiones y actividades al aire libre.",
        "fecha_salida": "15-01-2024",
        "fecha_llegada": "22-01-2024",
        "precio": 700.00
    },
    {
        "nombre": "Paquete Cultural",
        "descripcion": "Recorrido por ciudades con rica historia.",
        "fecha_salida": "05-02-2024",
        "fecha_llegada": "12-02-2024",
        "precio": 600.00
    },
    {
        "nombre": "Paquete Montaña",
        "descripcion": "Escapada a las montañas con actividades de senderismo.",
        "fecha_salida": "20-03-2024",
        "fecha_llegada": "27-03-2024",
        "precio": 650.00
    },
    {
        "nombre": "Paquete Gourmet",
        "descripcion": "Tour gastronómico por las mejores ciudades del país.",
        "fecha_salida": "10-04-2024",
        "fecha_llegada": "17-04-2024",
        "precio": 750.00
    },
    {
        "nombre": "Paquete Relax",
        "descripcion": "Estancia en un spa de lujo para relajarse.",
        "fecha_salida": "01-05-2024",
        "fecha_llegada": "08-05-2024",
        "precio": 800.00
    }
]

paquetes.extend(paquetes_preset)

def registrar_cliente():
    while True:
        nombre_completo = input("Ingrese nombre y apellido del cliente (ej. Juan Pérez): ")
        partes = nombre_completo.split()
        if len(partes) < 2:
            print("Error: Debe ingresar al menos un nombre y un apellido.")
            continue
        nombre = partes[0]
        apellido = " ".join(partes[1:]) 
        email = input("Ingrese email del cliente: ")
        telefono = input("Ingrese teléfono del cliente: ")
        clientes.append({"nombre": nombre, "apellido": apellido, "email": email, "telefono": telefono})
        print("Cliente registrado con éxito.")
        break

def crear_paquete():
    nombre = input("Ingrese nombre del paquete: ")
    descripcion = input("Ingrese descripcion del paquete: ")
    fecha_salida = input("Ingrese fecha de salida del paquete (dd-mm-aaaa): ")
    fecha_llegada = input("Ingrese fecha de llegada del paquete (dd-mm-aaaa): ")
    
    while True:
        try:
            precio = float(input("Ingrese precio del paquete: "))
            break
        except ValueError:
            print("Error: El precio debe ser un número.")

    paquetes.append({"nombre": nombre, "descripcion": descripcion, "fecha_salida": fecha_salida, "fecha_llegada": fecha_llegada, "precio": precio})
    print("Paquete creado con éxito.")

def realizar_reserva():
    while True:
        nombre_completo = input("Ingrese nombre y apellido del cliente: ")
        partes = nombre_completo.split()
        if len(partes) < 2:
            print("Error: Debe ingresar al menos un nombre y un apellido.")
            continue
        nombre_cliente = partes[0]
        apellido_cliente = " ".join(partes[1:]) 

        print("Paquetes disponibles para reservar:")
        mostrar_paquetes_numerados()

        while True:
            try:
                seleccion = int(input("Ingrese el número del paquete que desea reservar: "))
                if 1 <= seleccion <= len(paquetes):
                    nombre_paquete = paquetes[seleccion - 1]["nombre"]
                    break
                else:
                    print("Selección inválida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número.")

        for cliente in clientes:
            if cliente["nombre"] == nombre_cliente and cliente["apellido"] == apellido_cliente:
                for paquete in paquetes:
                    if paquete["nombre"] == nombre_paquete:
                        reservas.append({"cliente": cliente, "paquete": paquete})
                        print("Reserva realizada con éxito.")
                        return
        print("Cliente no encontrado.")
        break

def cancelar_reserva():
    while True:
        nombre_completo = input("Ingrese nombre y apellido del cliente: ")
        partes = nombre_completo.split()
        if len(partes) < 2:
            print("Error: Debe ingresar al menos un nombre y un apellido.")
            continue
        nombre_cliente = partes[0]
        apellido_cliente = " ".join(partes[1:]) 
        nombre_paquete = input("Ingrese nombre del paquete: ")
        
        for reserva in reservas:
            if (reserva["cliente"]["nombre"] == nombre_cliente and 
                reserva["cliente"]["apellido"] == apellido_cliente and 
                reserva["paquete"]["nombre"] == nombre_paquete):
                reservas.remove(reserva)
                print("Reserva cancelada con éxito.")
                return
        print("Reserva no encontrada.")
        break

def mostrar_reservas():
    print("Reservas:")
    for reserva in reservas:
        cliente = reserva['cliente']
        paquete = reserva['paquete']
        print(f"Cliente: {cliente['nombre']} {cliente['apellido']}")
        print(f"Paquete: {paquete['nombre']}")
        print(f"Fecha de salida: {paquete['fecha_salida']}")
        print(f"Fecha de llegada: {paquete['fecha_llegada']}")
        print(f"Precio: {paquete['precio']}")
        print("---------")

def mostrar_reservas_cliente():
    while True:
        nombre_completo = input("Ingrese nombre y apellido del cliente: ")
        partes = nombre_completo.split()
        if len(partes) < 2:
            print("Error: Debe ingresar al menos un nombre y un apellido.")
            continue
        nombre_cliente = partes[0]
        apellido_cliente = " ".join(partes[1:]) 
        print(f"Reservas de {nombre_cliente} {apellido_cliente}:")
        
        reservas_encontradas = False
        for reserva in reservas:
            if (reserva["cliente"]["nombre"] == nombre_cliente and 
                reserva["cliente"]["apellido"] == apellido_cliente):
                print(f"Paquete: {reserva['paquete']['nombre']}")
                print(f"Fecha de salida: {reserva['paquete']['fecha_salida']}")
                print(f"Fecha de llegada: {reserva['paquete']['fecha_llegada']}")
                print(f"Precio: {reserva['paquete']['precio']}")
                print("---------")
                reservas_encontradas = True
                
        if not reservas_encontradas:
            print("No se encontraron reservas para este cliente.")
        break

def mostrar_clientes():
    print("Clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
        print(f"Email: {cliente['email']}")
        print(f"Teléfono: {cliente['telefono']}")
        print("---------")

def mostrar_paquetes_numerados():
    print("Paquetes:")
    for index, paquete in enumerate(paquetes, start=1):
        print(f"{index}. {paquete['nombre']}")
        print(f"   Descripción: {paquete['descripcion']}")
        print(f"   Fecha de salida: {paquete['fecha_salida']}")
        print(f"   Fecha de llegada: {paquete['fecha_llegada']}")
        print(f"   Precio: {paquete['precio']}")
        print("---------")

def mostrar_paquetes_de_todos_los_clientes():
    print("Paquetes de todos los clientes:")
    for reserva in reservas:
        cliente = reserva["cliente"]
        paquete = reserva["paquete"]
        print(f"Cliente: {cliente['nombre']} {cliente['apellido']}")
        print(f"   Paquete: {paquete['nombre']}")
        print(f"   Descripción: {paquete['descripcion']}")
        print(f"   Fecha de salida: {paquete['fecha_salida']}")
        print(f"   Fecha de llegada: {paquete['fecha_llegada']}")
        print(f"   Precio: {paquete['precio']}")
        print("---------")

def eliminar_paquete():
    nombre_paquete = input("Escriba el nombre del paquete a eliminar: ")
    for paquete in paquetes:
        if paquete["nombre"] == nombre_paquete:
            confirmar = input(f"¿Está seguro de eliminar el paquete {nombre_paquete}? [SI o NO]: ").upper()
            if confirmar == "SI":
                paquetes.remove(paquete)
                print("Paquete eliminado exitosamente.")
                return
    print("Paquete no encontrado.")

def eliminar_cliente():
    nombre_completo = input("Escriba el nombre y apellido del cliente a eliminar: ")
    partes = nombre_completo.split()
    if len(partes) < 2:
        print("Error: Debe ingresar al menos un nombre y un apellido.")
        return
    nombre_cliente = partes[0]
    apellido_cliente = " ".join(partes[1:]) 

    for cliente in clientes:
        if cliente["nombre"] == nombre_cliente and cliente["apellido"] == apellido_cliente:
            confirmar = input(f"¿Está seguro de eliminar al cliente {nombre_completo}? [SI o NO]: ").upper()
            if confirmar == "SI":
                clientes.remove(cliente)
                reservas[:] = [reserva for reserva in reservas if reserva["cliente"] != cliente]
                print("Cliente eliminado exitosamente.")
                return
    print("Cliente no encontrado.")

def modificar_paquete():
    cambiar_paquete = input("Escriba el nombre del paquete a modificar: ")
    for paquete in paquetes:
        if paquete["nombre"] == cambiar_paquete:
            print("Ingrese nuevos datos (deje en blanco si va a mantener el dato actual): ")
            nuevo_nombre = input("Nombre: ") or paquete["nombre"]
            nueva_descripcion = input("Descripción: ") or paquete["descripcion"]
            nueva_fecha_salida = input("Fecha de salida (dd-mm-aaaa): ") or paquete["fecha_salida"]
            nueva_fecha_llegada = input("Fecha de llegada (dd-mm-aaaa): ") or paquete["fecha_llegada"]
            nuevo_precio = input("Precio: ") or paquete["precio"]

            paquete["nombre"] = nuevo_nombre
            paquete["descripcion"] = nueva_descripcion
            paquete["fecha_salida"] = nueva_fecha_salida
            paquete["fecha_llegada"] = nueva_fecha_llegada
            paquete["precio"] = float(nuevo_precio) if nuevo_precio else paquete["precio"]

            print("Paquete modificado con éxito.")
            return
    print("Paquete no encontrado.")

while True:
    print("Agencia de Viajes Global")
    for opcion, descripcion in menu.items():
        print(f"{opcion}. {descripcion}")
        
    opcion = input("Ingrese opción: ").strip()
    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        crear_paquete()
    elif opcion == "3":
        realizar_reserva()
    elif opcion == "4":
        cancelar_reserva()
    elif opcion == "5":
        mostrar_reservas()
    elif opcion == "6":
        mostrar_reservas_cliente() 
    elif opcion == "7":
        mostrar_clientes()
    elif opcion == "8":
        mostrar_paquetes_numerados()
    elif opcion == "9":
        eliminar_paquete()
    elif opcion == "10":
        eliminar_cliente() 
    elif opcion == "11":
        modificar_paquete()
    elif opcion == "12":  
        mostrar_paquetes_de_todos_los_clientes()
    elif opcion == "0":
        print("Gracias por utilizar nuestra agencia de viajes.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")