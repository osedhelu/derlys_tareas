# Programa para invertir un vector sin usar funciones predefinidas ni vector auxiliar

# Vector predefinido
vector = [10, 15, 80, 30, 90, 20, 50, 40, 70]
n = len(vector)

# Imprimir el vector inicial
print("\nVector inicial:")
for i in range(n):
    print(f"Posición {i+1}: {vector[i]}")

# Calcular la mitad del vector
mitad = n // 2

# Intercambiar los elementos
for i in range(mitad):
    # Calcular la posición opuesta
    pos_opuesta = n - 1 - i
    
    # Intercambiar los elementos
    temp = vector[i]
    vector[i] = vector[pos_opuesta]
    vector[pos_opuesta] = temp

# Imprimir el vector final
print("\nVector final:")
for i in range(n):
    print(f"Posición {i+1}: {vector[i]}") 