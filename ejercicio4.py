# Programa para calcular la suma acumulada de una lista

# Lista predefinida de ejemplo
lista = [1, 2, 3, 4, 5]

# Crear lista para la suma acumulada
suma_acumulada = [0] * len(lista)

# Calcular la suma acumulada
suma_actual = 0
for i in range(len(lista)):
    suma_actual = suma_actual + lista[i]
    suma_acumulada[i] = suma_actual

# Imprimir resultados
print("\nLista original:")
for i in range(len(lista)):
    print(f"Posición {i+1}: {lista[i]}")

print("\nLista con suma acumulada:")
for i in range(len(suma_acumulada)):
    print(f"Posición {i+1}: {suma_acumulada[i]}") 