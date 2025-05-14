#Desarrolla un algoritmo y un programa en Java que lea dos matrices A y B, 
# y genere una tercera matriz S que sea el resultado de la multiplicación de las matrices A y B. 
# Verifica que se pueda realizar la multiplicación


# Leer dimensiones de la matriz A
filas_A = int(input("Filas de A: "))
columnas_A = int(input("Columnas de A: "))

# Leer matriz A
A = []
for i in range(filas_A):
    fila = []
    for j in range(columnas_A):
        valor = int(input("A[" + str(i) + "][" + str(j) + "]: "))
        fila.append(valor)
    A.append(fila)

# Leer dimensiones de la matriz B
filas_B = int(input("Filas de B: "))
columnas_B = int(input("Columnas de B: "))

# Leer matriz B
B = []
for i in range(filas_B):
    fila = []
    for j in range(columnas_B):
        valor = int(input("B[" + str(i) + "][" + str(j) + "]: "))
        fila.append(valor)
    B.append(fila)

# Verificar si se pueden multiplicar
if columnas_A != filas_B:
    print("No se pueden multiplicar las matrices")
else:
    # Crear matriz resultado S con ceros
    S = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_B):
            fila.append(0)
        S.append(fila)

    # Multiplicación de matrices
    for i in range(filas_A):
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma = suma + A[i][k] * B[k][j]
            S[i][j] = suma

    # Mostrar matriz resultado
    print("Matriz resultado S:")
    for i in range(filas_A):
        for j in range(columnas_B):
            print(S[i][j], end=" ")
        print()