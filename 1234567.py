import datetime
import re

clientes = [{"nombre": "Mateo", "apellido": "Cardenas", "email": "mateo12@hotmail.com", "telefono": "3124567890", "documento": "123456789"},
            {"nombre": "Natalia", "apellido": "Lopez", "email": "naty@gmail.com", "telefono": "3204328899", "documento": "987654321"}]
paquetes = []
reservas = []

# Menú para cada tipo de usuario
menu_cliente = {
    "1": "Realizar reserva",
    "2": "Mostrar reservas",
    "3": "Mostrar paquetes",
    "4": "Editar reserva",
    "0": "Salir"
}

menu_administrador = {
    "1": "Registrar cliente",
    "2": "Crear paquete de viaje",
    "3": "Cancelar reserva",
    "4": "Mostrar reservas de un cliente",
    "5": "Mostrar clientes",
    "6": "Eliminar paquete",
    "7": "Modificar paquete",
    "8": "Editar cliente",
    "9": "Eliminar cliente",  # Nueva opción
    "0": "Salir"
}

# Paquetes de viaje predeterminados
paquetes_preset = [
    {"nombre": "Escapada a la Playa", "descripcion": "Disfruta de un fin de semana en la playa con todo incluido.", "fecha_salida": "01-10-2024", "fecha_llegada": "04-10-2024", "precio": 300.0},
    {"nombre": "Aventura en la Montaña", "descripcion": "Un emocionante viaje de senderismo y campamento.", "fecha_salida": "10-11-2024", "fecha_llegada": "15-11-2024", "precio": 450.0},
    # ... otros paquetes ...
]

paquetes.extend(paquetes_preset)

# Validaciones de clientes
def validar_nombre(nombre):
    patron = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')
    return bool(patron.fullmatch(nombre))

def validar_email(email):
    patron1 = re.compile(r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(patron1.fullmatch(email))

def validar_telefono(telefono):
    numero = re.compile(r'^\d{10}$')
    return bool(numero.fullmatch(telefono))

def validar_documento(documento):
    numero = re.compile(r'^\d+$')
    return bool(numero.fullmatch(documento))

def registrar_cliente():
    while True:
        nombre = input("Ingrese nombre del cliente: ")
        if validar_nombre(nombre):
            break
        else:
            print("Nombre inválido, NO puede contener números. Digite nuevamente.")
    
    while True:
        apellido = input("Ingrese apellido del cliente: ")
        if validar_nombre(apellido):
            break
        else:
            print("Apellido inválido, NO se admiten números. Digite nuevamente.")

    while True:
        email = input("Ingrese email del cliente: ")
        if validar_email(email):
            break
        else:
            print("Email NO Válido. Digíta nuevamente")

    while True:
        telefono = input("Ingrese teléfono del cliente: ")
        if validar_telefono(telefono):
            break
        else:
            print("Teléfono NO Válido. Deben ser 10 dígitos")

    while True:
        documento = input("Ingrese documento de identidad del cliente (solo números): ")
        if validar_documento(documento):
            break
        else:
            print("Documento inválido, debe contener solo números. Digite nuevamente.")

    clientes.append({"nombre": nombre, "apellido": apellido, "email": email, "telefono": telefono, "documento": documento})
    print("Cliente registrado con éxito.")

# Crear paquetes
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

# Verificar si el cliente está registrado
def cliente_registrado(nombre_cliente, apellido_cliente):
    for cliente in clientes:
        if cliente["nombre"] == nombre_cliente and cliente["apellido"] == apellido_cliente:
            return True
    return False

# Para que el cliente realice una reserva
def realizar_reserva():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")

    if not cliente_registrado(nombre_cliente, apellido_cliente):
        print("Cliente no registrado. Por favor registrese antes de realizar una reserva.")
        return

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
    print("Paquete no encontrado.")

# Editar reserva
def editar_reserva():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")

    if not cliente_registrado(nombre_cliente, apellido_cliente):
        print("Cliente no registrado. No puede editar reservas.")
        return

    mostrar_reservas_cliente(nombre_cliente, apellido_cliente)

    nombre_paquete_actual = input("Ingrese el nombre del paquete que desea editar: ")
    
    for reserva in reservas:
        if reserva["cliente"]["nombre"] == nombre_cliente and reserva["cliente"]["apellido"] == apellido_cliente and reserva["paquete"]["nombre"] == nombre_paquete_actual:
            print("Paquetes disponibles para seleccionar un nuevo paquete:")
            mostrar_paquetes_numerados()

            while True:
                try:
                    seleccion = int(input("Ingrese el número del nuevo paquete: "))
                    if 1 <= seleccion <= len(paquetes):
                        nuevo_paquete = paquetes[seleccion - 1]
                        reserva["paquete"] = nuevo_paquete
                        print("Reserva editada con éxito.")
                        return
                    else:
                        print("Selección inválida. Intente nuevamente.")
                except ValueError:
                    print("Error: Debe ingresar un número.")
    print("Reserva no encontrada.")

# Cancelación, mostrar de reservas
def cancelar_reserva():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")
    
    if not cliente_registrado(nombre_cliente, apellido_cliente):
        print("Cliente no registrado. No puede cancelar reservas.")
        return
    
    nombre_paquete = input("Ingrese nombre del paquete: ")
    
    for reserva in reservas:
        if reserva["cliente"]["nombre"] == nombre_cliente and reserva["cliente"]["apellido"] == apellido_cliente and reserva["paquete"]["nombre"] == nombre_paquete:
            reservas.remove(reserva)
            print("Reserva cancelada con éxito.")
            return
    print("Reserva no encontrada.")

def mostrar_reservas_cliente(nombre_cliente, apellido_cliente):
    print(f"Reservas de {nombre_cliente} {apellido_cliente}:")
    
    reservas_encontradas = False
    for reserva in reservas:
        if reserva["cliente"]["nombre"] == nombre_cliente and reserva["cliente"]["apellido"] == apellido_cliente:
            print(f"Paquete: {reserva['paquete']['nombre']}")
            print(f"Fecha de salida: {reserva['paquete']['fecha_salida']}")
            print(f"Fecha de llegada: {reserva['paquete']['fecha_llegada']}")
            print(f"Precio: {reserva['paquete']['precio']}")
            print("---------")
            reservas_encontradas = True
            
    if not reservas_encontradas:
        print("No se encontraron reservas para este cliente.")

def mostrar_paquetes_numerados():
    print("Paquetes:")
    for index, paquete in enumerate(paquetes, start=1):
        print(f"{index}. {paquete['nombre']}")
        print(f"   Descripción: {paquete['descripcion']}")
        print(f"   Fecha de salida: {paquete['fecha_salida']}")
        print(f"   Fecha de llegada: {paquete['fecha_llegada']}")
        print(f"   Precio: {paquete['precio']}")
        print("---------")

# Mostrar clientes 
def mostrar_clientes():
    print("Clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
        print(f"Email: {cliente['email']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Documento: {cliente['documento']}")
        print("---------")

# Editar cliente
def editar_cliente():
    documento = input("Ingrese documento del cliente a editar: ")
    for cliente in clientes:
        if cliente["documento"] == documento:
            print("Ingrese nuevos datos (deje en blanco si va a mantener el dato actual): ")
            nuevo_nombre = input("Nombre: ") or cliente["nombre"]
            nuevo_apellido = input("Apellido: ") or cliente["apellido"]
            nuevo_email = input("Email: ") or cliente["email"]
            nuevo_telefono = input("Teléfono: ") or cliente["telefono"]

            if nuevo_email and not validar_email(nuevo_email):
                print("Email inválido. No se ha realizado la actualización.")
                return

            if nuevo_telefono and not validar_telefono(nuevo_telefono):
                print("Teléfono inválido. No se ha realizado la actualización.")
                return

            cliente["nombre"] = nuevo_nombre
            cliente["apellido"] = nuevo_apellido
            cliente["email"] = nuevo_email
            cliente["telefono"] = nuevo_telefono

            print("Cliente editado con éxito.")
            return
    print("Cliente no encontrado.")

# Eliminar cliente
def eliminar_cliente():
    documento = input("Ingrese documento del cliente a eliminar: ")
    for cliente in clientes:
        if cliente["documento"] == documento:
            confirmar = input(f"¿Está seguro de eliminar al cliente {cliente['nombre']} {cliente['apellido']}? [SI o NO]: ").upper()
            if confirmar == "SI":
                clientes.remove(cliente)
                print("Cliente eliminado exitosamente.")
                return
            else:
                print("Operación cancelada.")
                return
    print("Cliente no encontrado.")

# Eliminar y modificar paquetes
def eliminar_paquete():
    nombre_paquete = input("Escriba el nombre del paquete a eliminar: ")
    for paquete in paquetes:
        if paquete["nombre"] == nombre_paquete:
            confirmar = input(f"¿Está seguro de eliminar el paquete {nombre_paquete}? [SI o NO]: ").upper()
            if confirmar == "SI":
                paquetes.remove(paquete)
                print("Paquete eliminado exitosamente.")
                return
            else:
                print("Operación cancelada.")
                return
    print("Paquete no encontrado.")

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

# Autenticación de administrador
def autenticar_administrador():
    contraseña = input("Ingrese la contraseña de administrador: ")
    return contraseña == "12345"

# Menú principal
def menu_principal():
    while True:
        print("Agencia de Viajes Global")
        tipo_usuario = input("¿Eres Cliente o Administrador? (C/A): ").strip().upper()
        
        if tipo_usuario == "C":
            while True:
                print("\n--- Menú Cliente ---")
                for opcion, descripcion in menu_cliente.items():
                    print(f"{opcion}. {descripcion}")

                opcion = input("Ingrese opción: ").strip()
                if opcion == "1":
                    realizar_reserva()
                elif opcion == "2":
                    mostrar_reservas_cliente(input("Ingrese nombre del cliente: "), input("Ingrese apellido del cliente: "))
                elif opcion == "3":
                    mostrar_paquetes_numerados()
                elif opcion == "4":
                    editar_reserva()
                elif opcion == "0":
                    print("Gracias por visitar nuestra agencia.")
                    break
                else:
                    print("Opción inválida.")
        
        elif tipo_usuario == "A":
            if autenticar_administrador():
                while True:
                    print("\n--- Menú Administrador ---")
                    for opcion, descripcion in menu_administrador.items():
                        print(f"{opcion}. {descripcion}")

                    opcion = input("Ingrese opción: ").strip()
                    if opcion == "1":
                        registrar_cliente()
                    elif opcion == "2":
                        crear_paquete()
                    elif opcion == "3":
                        cancelar_reserva()
                    elif opcion == "4":
                        mostrar_reservas_cliente(input("Ingrese nombre del cliente: "), input("Ingrese apellido del cliente: "))
                    elif opcion == "5":
                        mostrar_clientes()
                    elif opcion == "6":
                        eliminar_paquete()
                    elif opcion == "7":
                        modificar_paquete()
                    elif opcion == "8":
                        editar_cliente()
                    elif opcion == "9":
                        eliminar_cliente()  # Llamada a la nueva función
                    elif opcion == "0":
                        print("Gracias por utilizar nuestra agencia.")
                        break
                    else:
                        print("Opción inválida.")
            else:
                print("Contraseña incorrecta. Acceso denegado.")
        
        else:
            print("Opción inválida. Por favor, ingrese C para Cliente o A para Administrador.")

menu_principal()
