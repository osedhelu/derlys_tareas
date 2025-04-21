# Programa para encontrar estudiantes que ganaron ambas asignaturas

# Vectores predefinidos de ejemplo
matematicas = [1001, 1002, 1003, 1004, 1005]
fisica = [1002, 1004, 1006, 1007, 1008]

# Crear lista para los estudiantes que ganaron ambas asignaturas
ganados = []

# Encontrar estudiantes que ganaron ambas asignaturas
for codigo in matematicas:
    # Verificar si el código está en física
    for codigo_fisica in fisica:
        if codigo == codigo_fisica:
            ganados.append(codigo)
            break  # Salir del bucle interno si encontramos coincidencia

# Imprimir resultados
print("\nEstudiantes que ganaron Matemáticas:")
for i in range(len(matematicas)):
    print(f"Posición {i+1}: {matematicas[i]}")

print("\nEstudiantes que ganaron Física:")
for i in range(len(fisica)):
    print(f"Posición {i+1}: {fisica[i]}")

print("\nEstudiantes que ganaron ambas asignaturas:")
if len(ganados) > 0:
    for i in range(len(ganados)):
        print(f"Posición {i+1}: {ganados[i]}")
else:
    print("No hay estudiantes que hayan ganado ambas asignaturas") 