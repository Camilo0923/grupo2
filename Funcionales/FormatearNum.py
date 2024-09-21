#Duncion personalizada para formatear los numeros con separadores
#de miles y decimales (Estilo Colombiano)

def formatearNum(numero):
    numFormateado = f"{numero:,.2f}" 
    return  numFormateado.replace(",","_").replace(".",",").replace("_",".")


numero = 7654789.887
print(formatearNum(numero))
