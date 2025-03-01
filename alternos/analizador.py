# Tabla de transiciones representada como un diccionario
Tabla = {
    (1, "digito"): 2, (1, "."): "error", (1, "E"): "error", (1, "+"): "error", (1, "-"): "error", (1, "FDC"): "error",
    (2, "digito"): 2, (2, "."): 3, (2, "E"): 5, (2, "+"): "error", (2, "-"): "error", (2, "FDC"): "aceptar",
    (3, "digito"): 4, (3, "."): "error", (3, "E"): "error", (3, "+"): "error", (3, "-"): "error", (3, "FDC"): "error",
    (4, "digito"): 4, (4, "."): "error", (4, "E"): 5, (4, "+"): "error", (4, "-"): "error", (4, "FDC"): "aceptar",
    (5, "digito"): 7, (5, "."): "error", (5, "E"): "error", (5, "+"): 6, (5, "-"): 6, (5, "FDC"): "error",
    (6, "digito"): 7, (6, "."): "error", (6, "E"): "error", (6, "+"): "error", (6, "-"): "error", (6, "FDC"): "error",
    (7, "digito"): 7, (7, "."): "error", (7, "E"): "error", (7, "+"): "error", (7, "-"): "error", (7, "FDC"): "aceptar",
}

# Función para clasificar los símbolos de entrada
def clasificar_simbolo(simbolo):
    if simbolo.isdigit():
        return "digito"
    elif simbolo in {".", "E", "+", "-"}:
        return simbolo
    elif simbolo == "":  # Fin de cadena
        return "FDC"
    else:
        return "error"

# Función principal para el análisis léxico
def analizador_lexico(cadena):
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

        if entrada == "error" or (estado, entrada) not in Tabla:
            print(f"❌ No hay transición para (estado {estado}, entrada '{entrada}')")
            return "Error léxico"

        estado = Tabla[(estado, entrada)]
        print(f"✅ Nuevo estado: {estado}")

    print("🎉 Cadena aceptada")
    return "Cadena aceptada"

# Ejemplo de uso
cadena = "123.45E+6"
print(analizador_lexico(cadena))  # Debería imprimir "Cadena aceptada"
