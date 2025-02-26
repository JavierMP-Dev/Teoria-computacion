def leer_tabla_desde_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    # Leer símbolos
    simbolos = lineas[0].strip().split()

    # Construir la tabla de transiciones
    tabla = {}
    for linea in lineas[1:]:
        partes = linea.strip().split()
        estado = int(partes[0])  # Estado inicial de la fila
        for i, valor in enumerate(partes[1:]):
            tabla[(estado, simbolos[i])] = int(valor) if valor.isdigit() else valor

    return tabla


def clasificar_simbolo(simbolo):
    if simbolo.isdigit():
        return "digito"
    elif simbolo in {".", "E", "+", "-"}:
        return simbolo
    elif simbolo == "":  # Fin de cadena
        return "FDC"
    else:
        return "error"


def analizador_lexico(cadena, tabla):
    estado = 1
    i = 0
    print(f"Inicio del análisis: Estado = {estado}")

    while estado != "aceptar":
        if estado == "error":
            print(f"❌ Error léxico en el carácter '{cadena[i-1]}' (posición {i-1})")
            return "Error léxico"

        if i < len(cadena):
            simbolo = cadena[i]
            i += 1
        else:
            simbolo = ""

        entrada = clasificar_simbolo(simbolo)
        print(f"🧐 Procesando '{simbolo}' → Clasificado como: {entrada}")

        if entrada == "error" or (estado, entrada) not in tabla:
            print(f"❌ No hay transición para (estado {estado}, entrada '{entrada}')")
            return "Error léxico"

        estado = tabla[(estado, entrada)]
        print(f" Nuevo estado: {estado}")

   
    return "Cadena aceptada"


# Cargar tabla de transiciones desde archivo
nombre_archivo = "tabla.txt"
tabla = leer_tabla_desde_archivo(nombre_archivo)

# Probar con una cadena tabla 1
#cadena = "123.45E+6"

# Probar con una cadena tabla 2
cadena = "12.34E+5" 


# Probar con una cadena tabla 3
#cadena = "110011"

# Probar con una cadena tabla 4
#cadena = "+"

print(analizador_lexico(cadena, tabla))
