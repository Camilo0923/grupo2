def capturar_nota(prueba):
    while True:
        try:
            nota = float(input(f"Nota {prueba}: "))
            if 0.0 <= nota <= 5.0:
                return nota
            else:
                print(f"La nota del {prueba} debe estar entre 0.0 y 5.0. Inténtelo de nuevo.")
        except ValueError:
            print("Error: La nota ingresada no es válida. Debe ser un número.")

def main():
    
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("Advertencia: El nombre del estudiante no puede estar vacío.")
        return

    
    codigo = input("Código: ").strip()

    
    primer_parcial = capturar_nota("Primer Parcial")
    segundo_parcial = capturar_nota("Segundo Parcial")
    examen_final = capturar_nota("Examen Final")

    
    nota_definitiva = (primer_parcial * 0.35) + (segundo_parcial * 0.35) + (examen_final * 0.30)

    
    if nota_definitiva > 3.5:
        print(f"La nota final de {nombre} es {nota_definitiva:.1f}, por lo tanto APRUEBA.")
    elif nota_definitiva <= 3.5:
        print(f"La nota final de {nombre} es {nota_definitiva:.1f}, por lo tanto NO APRUEBA.")

if __name__ == "__main__":
    main()
