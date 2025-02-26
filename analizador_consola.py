def leer_tabla_desde_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = [linea.strip() for linea in archivo.readlines() if linea.strip()]  # Elimina líneas vacías

    # Leer símbolos (primera línea)
    simbolos = lineas[0].split(",")

    # Construir la tabla de transiciones
    tabla = {}
    estados_finales = set()
    
    for linea in lineas[1:]:
        if linea.startswith("F:"):  # Línea de estados de aceptación
            estados_finales = set(map(int, linea[2:].split(",")))  # Convierte a enteros
            continue

        partes = linea.split(":")
        if len(partes) != 2:
            print(f"⚠️ Error en línea: {linea} → Formato incorrecto")
            continue  # Salta la línea incorrecta

        try:
            estado = int(partes[0].strip())  # Convertir el estado a entero
        except ValueError:
            print(f"⚠️ Error: Estado no válido en línea → {linea}")
            continue

        transiciones = partes[1].split(",")
        if len(transiciones) != len(simbolos):
            print(f"⚠️ Advertencia: Cantidad de transiciones incorrecta en línea → {linea}")

        for i, valor in enumerate(transiciones):
            tabla[(estado, simbolos[i])] = int(valor) if valor.isdigit() else "error"

    return tabla, estados_finales



def clasificar_simbolo(simbolo, simbolos_validos):
    if simbolo in simbolos_validos:
        return simbolo
    else:
        return "error"


def analizador_lexico(cadena, tabla, estados_finales, simbolos_validos):
    estado = 1
    i = 0
    print(f"Inicio del análisis: Estado = {estado}")

    while i < len(cadena):
        simbolo = cadena[i]
        i += 1

        entrada = clasificar_simbolo(simbolo, simbolos_validos)
        print(f"🧐 Procesando '{simbolo}' → Clasificado como: {entrada}")

        if entrada == "error" or (estado, entrada) not in tabla:
            print(f"❌ No hay transición para (estado {estado}, entrada '{entrada}')")
            return "Error léxico"

        estado = tabla[(estado, entrada)]
        print(f"✅ Nuevo estado: {estado}")

    if estado in estados_finales:
        print("🎉 Cadena aceptada")
        return "Cadena aceptada"
    else:
        print("❌ Estado final no válido")
        return "Error léxico"


# Pedir el archivo y la cadena por consola
nombre_archivo = input("📂 Ingresa el nombre del archivo de la tabla: ")
cadena = input("🔢 Ingresa la cadena a analizar: ")

# Cargar tabla de transiciones desde archivo
tabla, estados_finales = leer_tabla_desde_archivo(nombre_archivo)

# Extraer los símbolos válidos de la tabla
simbolos_validos = {key[1] for key in tabla.keys()}

# Analizar la cadena ingresada
resultado = analizador_lexico(cadena, tabla, estados_finales, simbolos_validos)
print(f"📝 Resultado: {resultado}")
