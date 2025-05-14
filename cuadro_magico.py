# Un cuadrado mágico de 3 x 3 es una matriz de 3 x 3 formada por números del 1 al 9, 
# en la que la suma de sus filas, columnas y diagonales es idéntica. Desarrolla un algoritmo 
# y un programa en python que permita ingresar un cuadrado por teclado y determinar si es mágico o no.
#  El programa debe validar que los números ingresados estén dentro del rango de 1 a 9.

def ingresar_cuadrado():
    """
    Permite al usuario ingresar los números de un cuadrado 3x3 por teclado.
    Valida que cada número esté entre 1 y 9.
    Retorna el cuadrado como una lista de listas.
    """
    cuadrado = []
    print("Ingrese los números para el cuadrado (del 1 al 9):")
    for i in range(3):
        fila_actual = []
        # Usamos i_mas_uno para el mensaje al usuario, ya que las filas son 1, 2, 3.
        i_mas_uno = i + 1
        print("Fila", i_mas_uno, ":")
        for j in range(3):
            while True:
                # Usamos j_mas_uno para el mensaje al usuario.
                j_mas_uno = j + 1
                # Para construir el mensaje de input, concatenamos cadenas y la conversión de j_mas_uno a cadena.
                # No se pueden usar f-strings ni format() bajo las restricciones.
                # Se asume que input() y str() están permitidos como funciones básicas.
                mensaje_input = "  Ingrese el número para la columna " + str(j_mas_uno) + ": "
                numero_str = input(mensaje_input)
                
                # Validar si la entrada es un número antes de convertir es complejo sin try-except o isdigit.
                # Se asumirá que el usuario ingresa un número entero.
                # La función int() se usa para convertir, y puede generar un error si la entrada no es un número válido.
                # Esto es una limitación dadas las restricciones.
                valor_ingresado = int(numero_str)

                if valor_ingresado >= 1 and valor_ingresado <= 9:
                    fila_actual.append(valor_ingresado)
                    break
                else:
                    # Mensaje de error si el número no está en el rango.
                    mensaje_error = "Número inválido. Debe estar entre 1 y 9. Intente de nuevo."
                    print(mensaje_error)
        cuadrado.append(fila_actual)
    return cuadrado

def es_magico(cuadrado):
    """
    Verifica si un cuadrado 3x3 es mágico.
    Un cuadrado es mágico si la suma de sus filas, columnas y diagonales es idéntica.
    Se asume que el cuadrado tiene dimensiones 3x3 y los números ya fueron validados (rango 1-9).
    """
    # Calcular la suma de referencia (usando la primera fila)
    # No podemos usar sum(), así que iteramos.
    suma_referencia = 0
    # Calculamos la longitud de la primera fila para el bucle.
    longitud_fila_0 = len(cuadrado[0])
    for k_idx in range(longitud_fila_0):
        suma_referencia = suma_referencia + cuadrado[0][k_idx]

    # Verificar sumas de las filas
    longitud_cuadrado = len(cuadrado) # Número de filas
    for i in range(longitud_cuadrado):
        suma_fila_actual = 0
        longitud_fila_i = len(cuadrado[i]) # Número de columnas en la fila actual
        for j in range(longitud_fila_i):
            suma_fila_actual = suma_fila_actual + cuadrado[i][j]
        if suma_fila_actual != suma_referencia:
            return False

    # Verificar sumas de las columnas
    # Asumimos que es un cuadrado, len(cuadrado[0]) es el num de columnas
    num_columnas = len(cuadrado[0]) 
    for j in range(num_columnas):
        suma_columna_actual = 0
        for i in range(longitud_cuadrado): # Itera sobre las filas
            suma_columna_actual = suma_columna_actual + cuadrado[i][j]
        if suma_columna_actual != suma_referencia:
            return False

    # Verificar suma de la diagonal principal (izquierda-arriba a derecha-abajo)
    suma_diag_principal = 0
    for i in range(longitud_cuadrado): # El cuadrado es NxN, así que len(cuadrado) sirve para filas y columnas
        suma_diag_principal = suma_diag_principal + cuadrado[i][i]
    if suma_diag_principal != suma_referencia:
        return False

    # Verificar suma de la diagonal secundaria (derecha-arriba a izquierda-abajo)
    suma_diag_secundaria = 0
    # El índice de la columna para la diagonal secundaria es len(cuadrado) - 1 - i
    indice_base_diag_sec = longitud_cuadrado - 1
    for i in range(longitud_cuadrado):
        suma_diag_secundaria = suma_diag_secundaria + cuadrado[i][indice_base_diag_sec - i]
    if suma_diag_secundaria != suma_referencia:
        return False

    # Si todas las sumas coinciden
    return True

# --- Programa Principal ---

# Obtener el cuadrado del usuario
mi_cuadrado = ingresar_cuadrado()

# Imprimir el cuadrado ingresado para verificación
# No se pueden usar f-strings, join, o métodos de string complejos.
print("\nCuadrado ingresado:") # Usamos \n para el salto de línea literal
longitud_mi_cuadrado = len(mi_cuadrado)
for i in range(longitud_mi_cuadrado):
    longitud_fila_actual = len(mi_cuadrado[i])
    for j in range(longitud_fila_actual):
        # print() por defecto añade un salto de línea. Usamos end=" " para evitarlo.
        # str() convierte el número a cadena para que print pueda manejarlo con end=" ".
        print(str(mi_cuadrado[i][j]), end=" ") 
    print() # Nueva línea después de cada fila

# Determinar si es mágico e imprimir el resultado
if es_magico(mi_cuadrado):
    print("\n¡El cuadrado es mágico!")
else:
    print("\nEl cuadrado NO es mágico.")