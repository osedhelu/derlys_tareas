# Programa para calcular sumatoria de positivos múltiplos de 7 y productoria de negativos

# Lista predefinida de ejemplo
lista = [14, -3, 21, -5, 7, -2, 28, -1, 35]

# Inicializar variables
sumatoria = 0
productoria = 1
hay_negativos = False

# Calcular sumatoria de positivos múltiplos de 7 y productoria de negativos
for numero in lista:
    # Verificar si es positivo y múltiplo de 7
    if numero > 0 and numero % 7 == 0:
        sumatoria = sumatoria + numero
    
    # Verificar si es negativo
    if numero < 0:
        productoria = productoria * numero
        hay_negativos = True

# Imprimir resultados
print("\nLista de números:")
for i in range(len(lista)):
    print(f"Posición {i+1}: {lista[i]}")

print(f"\nSumatoria de positivos múltiplos de 7: {sumatoria}")

if hay_negativos:
    print(f"Productoria de números negativos: {productoria}")
else:
    print("No hay números negativos en la lista") 