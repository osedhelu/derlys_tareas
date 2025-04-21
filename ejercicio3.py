# Programa para generar una lista C a partir de dos listas A y B

# Listas predefinidas de ejemplo
A = [10, 15, 20, 25, 30]
B = [5, 10, 15, 20, 25]

# Obtener el tamaño de las listas
M = len(A)

# Crear lista C vacía
C = [0] * M

# Calcular los elementos de C
for i in range(M):
    # Verificar si la posición es par o impar
    if i % 2 == 0:  # Si es par
        C[i] = A[i] + B[i] - 2
    else:  # Si es impar
        C[i] = A[i] - B[i] + 7

# Imprimir las tres listas
print("\nLista A:")
for i in range(M):
    print(f"Posición {i+1}: {A[i]}")

print("\nLista B:")
for i in range(M):
    print(f"Posición {i+1}: {B[i]}")

print("\nLista C:")
for i in range(M):
    print(f"Posición {i+1}: {C[i]}") 