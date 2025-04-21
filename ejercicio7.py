# Programa para generar serie de Fibonacci y sumar elementos pares

# Leer el número N
N = int(input("Ingrese el número de términos de Fibonacci a generar: "))

# Crear vector para almacenar la serie
fibonacci = [0] * N

# Generar los primeros N términos de Fibonacci
if N >= 1:
    fibonacci[0] = 0
if N >= 2:
    fibonacci[1] = 1

for i in range(2, N):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

# Calcular suma de elementos pares
suma_pares = 0
for numero in fibonacci:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero

# Imprimir resultados
print("\nSerie de Fibonacci generada:")
for i in range(N):
    print(f"Posición {i+1}: {fibonacci[i]}")

print(f"\nSuma de los elementos pares: {suma_pares}") 