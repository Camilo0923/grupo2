clientes = [] 
paquetes = []
reservas = []

menu = {
    "1": "Registrar cliente",
    "2": "Crear paquete de viaje",
    "3": "Editar paquete de viaje",
    "4": "Realizar reserva",
    "5": "Cancelar reserva",
    "6": "Mostrar reservas",
    "7": "Mostrar clientes",
    "8": "Mostrar paquetes",
    "9": "Salir"
}

def registrar_cliente():
    nombre = input("Ingrese nombre y apellido del cliente: ")
    email = input("Ingrese email del cliente: ")
    telefono = input("Ingrese teléfono del cliente: ")
    clientes.append({"nombre": nombre, "email": email, "telefono": telefono, "reservas": []})
    print("Cliente registrado con éxito.")

def crear_paquete():
    nombre = input("Ingrese nombre del paquete: ")
    destino = input("Ingrese destino del paquete: ")
    fecha_salida = input("Ingrese fecha de salida del paquete (dd-mm-aaaa): ")
    fecha_llegada = input("Ingrese fecha de llegada del paquete (dd-mm-aaaa): ")
    
    actividades = input("Ingrese actividades incluidas en el paquete (separadas por comas): ").split(",")
    while True:
        try:
            precio = float(input("Ingrese precio del paquete: "))
            break
        except ValueError:
            print("Error: El precio debe ser un número.")

    paquetes.append({
        "nombre": nombre,
        "destino": destino,
        "fecha_salida": fecha_salida,
        "fecha_llegada": fecha_llegada,
        "precio": precio,
        "actividades": [actividad.strip() for actividad in actividades]
    })
    print("Paquete creado con éxito.")

def editar_paquete():
    nombre_paquete = input("Ingrese el nombre del paquete que desea editar: ")
    for paquete in paquetes:
        if paquete["nombre"] == nombre_paquete:
            print("Paquete encontrado. Ingrese los nuevos datos o presione Enter para mantener el actual.")
            nuevo_nombre = input(f"Nuevo nombre (actual: {paquete['nombre']}): ") or paquete["nombre"]
            nuevo_destino = input(f"Nuevo destino (actual: {paquete['destino']}): ") or paquete["destino"]
            nuevo_fecha_salida = input(f"Nueva fecha de salida (actual: {paquete['fecha_salida']}): ") or paquete["fecha_salida"]
            nuevo_fecha_llegada = input(f"Nueva fecha de llegada (actual: {paquete['fecha_llegada']}): ") or paquete["fecha_llegada"]
            
            actividades = input("Nuevas actividades (separadas por comas, actual: {}): ".format(", ".join(paquete["actividades"]))) or ", ".join(paquete["actividades"])
            nuevo_precio = input(f"Nuevo precio (actual: {paquete['precio']}): ")
            nuevo_precio = float(nuevo_precio) if nuevo_precio else paquete["precio"]
            
            paquete.update({
                "nombre": nuevo_nombre,
                "destino": nuevo_destino,
                "fecha_salida": nuevo_fecha_salida,
                "fecha_llegada": nuevo_fecha_llegada,
                "precio": nuevo_precio,
                "actividades": [actividad.strip() for actividad in actividades.split(",")]
            })
            print("Paquete actualizado con éxito.")
            return
    print("Paquete no encontrado.")

def realizar_reserva():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")
    nombre_paquete = input("Ingrese nombre del paquete: ")
    
    for cliente in clientes:
        if cliente["nombre"] == nombre_cliente and cliente["apellido"] == apellido_cliente:
            for paquete in paquetes:
                if paquete["nombre"] == nombre_paquete:
                    reserva = {"cliente": cliente, "paquete": paquete}
                    reservas.append(reserva)
                    cliente["reservas"].append(reserva)
                    print("Reserva realizada con éxito.")
                    return
            print("Paquete no encontrado.")
            return
    print("Cliente no encontrado.")

def cancelar_reserva():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")
    nombre_paquete = input("Ingrese nombre del paquete: ")
    
    for reserva in reservas:
        if reserva["cliente"]["nombre"] == nombre_cliente and reserva["cliente"]["apellido"] == apellido_cliente and reserva["paquete"]["nombre"] == nombre_paquete:
            reservas.remove(reserva)
            reserva["cliente"]["reservas"].remove(reserva)
            print("Reserva cancelada con éxito.")
            return
    print("Reserva no encontrada.")

def mostrar_reservas():
    print("Reservas:")
    for reserva in reservas:
        print(f"Cliente: {reserva['cliente']['nombre']} {reserva['cliente']['apellido']}")
        print(f"Paquete: {reserva['paquete']['nombre']}")
        print(f"Fecha de salida: {reserva['paquete']['fecha_salida']}")
        print(f"Fecha de llegada: {reserva['paquete']['fecha_llegada']}")
        print(f"Precio: {reserva['paquete']['precio']}")
        print("Actividades: " + ", ".join(reserva['paquete']['actividades']))
        print("---------")

def mostrar_clientes():
    print("Clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
        print(f"Email: {cliente['email']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Historial de reservas: {[reserva['paquete']['nombre'] for reserva in cliente['reservas']]}")
        print("---------")

def mostrar_paquetes():
    print("Paquetes:")
    for paquete in paquetes:
        print(f"Nombre: {paquete['nombre']}")
        print(f"Destino: {paquete['destino']}")
        print(f"Fecha de salida: {paquete['fecha_salida']}")
        print(f"Fecha de llegada: {paquete['fecha_llegada']}")
        print(f"Precio: {paquete['precio']}")
        print(f"Actividades: {', '.join(paquete['actividades'])}")
        print("---------")

while True:
    print("Agencia de Viajes")
    for opcion, descripcion in menu.items():
        print(f"{opcion}. {descripcion}")
        
    opcion = input("Ingrese opción: ").strip()
    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        crear_paquete()
    elif opcion == "3":
        editar_paquete()
    elif opcion == "4":
        realizar_reserva()
    elif opcion == "5":
        cancelar_reserva()
    elif opcion == "6":
        mostrar_reservas()
    elif opcion == "7":
        mostrar_clientes()
    elif opcion == "8":
        mostrar_paquetes()
    elif opcion == "9":
        print("Gracias por utilizar nuestra agencia de viajes.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
