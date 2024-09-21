"""
Actividad 1:  Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente, su precio y calcular el total a pagar.
Diseña un programa con las siguientes características:
1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
2. Una variable total que vaya sumando el precio de los artículos
3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y el precio de cada producto y los imprima.
 4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
5. Si no hay más artículos, que imprima el total de la compra
Al final de tus funciones, puedes simplemente llamar a la función caja para probar: caja()


def caja(nombre, precio):
    
   # Imprime el nombre y el precio del producto.
    
    print(f"Producto: {nombre}, Precio: ${precio:.2f}")

def caja():
    
    # Función principal que gestiona la entrada de productos y el cálculo total de la compra.
    
    total = 0.0
    
    while True:
        # Solicita el nombre del producto
        nombre = input("Ingrese el nombre del producto: ").strip()
        
        # Solicita el precio del producto
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: $"))
                if precio >= 0:
                    break
                else:
                    print("El precio no puede ser negativo. Inténtelo de nuevo.")
            except ValueError:
                print("Error: El precio ingresado no es válido. Debe ser un número.")
        
        # Imprime el producto y su precio
        imprimeProducto(nombre, precio)
        
        # Suma el precio al total
        total += precio
        
        # Pregunta si hay más artículos
        mas_articulos = input("¿Tiene más artículos para ingresar? (sí/no): ").strip().lower()
        
        if mas_articulos != 'sí' and mas_articulos != 's':
            break
    
    # Imprime el total de la compra
    print(f"Total a pagar: ${total:.2f}")

# Llama a la función caja para ejecutar el programa
caja()
"""
