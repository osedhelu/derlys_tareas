def ingresar_datos_cultivos():
    print("---  Cultivos de Sorgo y Maíz ---")
    n = int(input("Ingrese el número de años a analizar: "))
    matriz = []
    for i in range(n):
        print(f"\nAño {i+1}:")
        anio = int(input("  Ingrese el año: "))
        sorgo = int(input("  Hectáreas de sorgo: "))
        maiz = int(input("  Hectáreas de maíz: "))
        matriz.append([anio, sorgo, maiz])
    return matriz

def analizar_cultivos(matriz):
    n = len(matriz)
    if n == 0:
        print("No hay datos para analizar.")
        return

    # 1. Año(s) con menor cantidad de hectáreas de sorgo
    min_sorgo = matriz[0][1]
    for fila in matriz:
        if fila[1] < min_sorgo:
            min_sorgo = fila[1]
    anios_min_sorgo = []
    for fila in matriz:
        if fila[1] == min_sorgo:
            anios_min_sorgo.append(fila[0])

    # 2. Año(s) con igual cantidad de sorgo y maíz
    anios_igual = []
    for fila in matriz:
        if fila[1] == fila[2]:
            anios_igual.append(fila[0])

    # 3. Año(s) con mayor incremento de sorgo respecto al año anterior
    max_incremento = None
    anios_max_incremento = []
    for i in range(1, n):
        incremento = matriz[i][1] - matriz[i-1][1]
        if max_incremento is None or incremento > max_incremento:
            max_incremento = incremento
    for i in range(1, n):
        incremento = matriz[i][1] - matriz[i-1][1]
        if incremento == max_incremento:
            anios_max_incremento.append(matriz[i][0])

    # 4. Año(s) con mayor cantidad absoluta entre sorgo y maíz
    max_cereal = None
    anios_max_cereal = []
    for fila in matriz:
        mayor = max(fila[1], fila[2])
        if max_cereal is None or mayor > max_cereal:
            max_cereal = mayor
    for fila in matriz:
        if fila[1] == max_cereal or fila[2] == max_cereal:
            anios_max_cereal.append(fila[0])

    # Imprimir resultados
    print("\n--- Resultados del Análisis ---")
    print(f"Año(s) con menor cantidad de hectáreas de sorgo: {anios_min_sorgo}")
    if anios_igual:
        print(f"Año(s) con igual cantidad de sorgo y maíz: {anios_igual}")
    else:
        print("Ningún año tuvo igual cantidad de sorgo y maíz.")
    print(f"Año(s) con mayor incremento de sorgo respecto al año anterior: {anios_max_incremento}")
    print(f"Año(s) con mayor cantidad absoluta entre sorgo y maíz: {anios_max_cereal}")

# --- Ejecución principal ---
matriz = ingresar_datos_cultivos()
analizar_cultivos(matriz)
print("\n--- Fin del Programa ---")
