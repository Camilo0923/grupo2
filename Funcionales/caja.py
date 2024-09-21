
def imprimaproducto(nombre, precio):
    print(f"producto {nombre}: ${precio} ")

def caja():
    nombreprod = input("ingrese nombre delproducto")
    precioprod = int(input(f"Ingrese precio del producto {nombreprod} "))
    total=precioprod
    imprimaproducto(nombreprod,precioprod)
    while True:
        respuesta = input("¿Desea ingresar mas prodictos? [si - no] : ").lowerU()
        if respuesta.strip == "si":
            nombreprod = input("ingrese nombre del producto: ")
            precioprod = int(input(f"ingrese precio del producto {nombreprod}: "))
            total+=precioprod
            imprimaproducto(nombreprod,precioprod)
        else:
            break
    print(f"El total de la compra es {total}")

caja() 
