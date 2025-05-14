print("--- Análisis de Cultivos de Sorgo y Maíz ---")
n = int(input("Ingrese el número de años a analizar: "))
matriz = []
for i in range(n):
    print(f"\nAño {i+1}:")
    anio = int(input("  Año: "))
    sorgo = int(input("  Sorgo: "))
    maiz = int(input("  Maíz: "))
    matriz.append([anio, sorgo, maiz])

# 1. Menor sorgo
min_sorgo = min(fila[1] for fila in matriz)
anios_min_sorgo = [fila[0] for fila in matriz if fila[1] == min_sorgo]

# 2. Igual sorgo y maíz
anios_igual = [fila[0] for fila in matriz if fila[1] == fila[2]]

# 3. Mayor incremento de sorgo
incrementos = [matriz[i][1] - matriz[i-1][1] for i in range(1, n)]
if incrementos:
    max_inc = max(incrementos)
    anios_max_inc = [matriz[i][0] for i in range(1, n) if matriz[i][1] - matriz[i-1][1] == max_inc]
else:
    anios_max_inc = []

# 4. Mayor cantidad absoluta entre sorgo y maíz
max_cereal = max(max(fila[1], fila[2]) for fila in matriz)
anios_max_cereal = [fila[0] for fila in matriz if fila[1] == max_cereal or fila[2] == max_cereal]

print("\n--- Resultados ---")
print("Año(s) con menor sorgo:", anios_min_sorgo)
print("Año(s) con igual sorgo y maíz:", anios_igual if anios_igual else "Ninguno")
print("Año(s) con mayor incremento de sorgo:", anios_max_inc)
print("Año(s) con mayor cantidad absoluta entre sorgo y maíz:", anios_max_cereal)
print("\n--- Fin del Programa ---") 