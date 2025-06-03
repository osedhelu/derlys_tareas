def obtener_tamano_matriz():
    """
    Solicita al usuario el tamaño de la matriz cuadrada (M).
    Valida que sea un entero positivo.
    Returns:
        int: El tamaño M de la matriz, o 0 si la entrada no es válida o es <= 0.
    """
    while True:
        try:
            m = int(input("Ingrese el tamaño de la matriz cuadrada (M x M, M debe ser > 0): "))
            if m > 0:
                return m
            else:
                print("El tamaño debe ser un número entero positivo. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero. Intente de nuevo.")

def ingresar_elementos_matriz(m_tamano):
    """
    Permite al usuario ingresar los elementos de una matriz cuadrada.
    Args:
        m_tamano (int): El tamaño (M) de la matriz.
    Returns:
        list: La matriz (lista de listas) con los elementos ingresados.
    """
    matriz = []
    print(f"\nIngrese los elementos para la matriz de {m_tamano}x{m_tamano}:")
    for i in range(m_tamano):
        fila_actual = []
        print(f"--- Fila {i + 1} ---")
        for j in range(m_tamano):
            while True:
                try:
                    elemento = int(input(f"  Elemento para posición ({i + 1},{j + 1}): "))
                    fila_actual.append(elemento)
                    break # Sale del bucle de reintento si la entrada es válida
                except ValueError:
                    print("  Entrada no válida. Por favor, ingrese un número entero.")
        matriz.append(fila_actual)
    return matriz

def imprimir_matriz(matriz, titulo="Matriz"):
    """
    Imprime una matriz en la consola de forma legible.
    Args:
        matriz (list): La matriz (lista de listas) a imprimir.
        titulo (str): Un título opcional para mostrar antes de la matriz.
    """
    print(f"\n{titulo}:")
    if not matriz: # Si la matriz está vacía
        print("  (Matriz vacía)")
        return
    for fila in matriz:
        fila_formateada = ""
        for elemento_idx in range(len(fila)):
            # Ajustar el espaciado para una mejor alineación (simple)
            fila_formateada = fila_formateada + str(fila[elemento_idx])
            if elemento_idx < len(fila) - 1:
                 fila_formateada = fila_formateada + "\t" # Usar tabulación para separar
        print(f"  {fila_formateada}")

def poner_ceros_en_diagonales(matriz):
    """
    Modifica la matriz dada (cuadrada) para poner ceros en su diagonal principal y secundaria.
    La matriz se modifica en el lugar (in-place).
    Args:
        matriz (list): La matriz (lista de listas) a modificar.
    """
    if not matriz or not matriz[0]: # Si la matriz está vacía o no tiene filas/columnas
        return
        
    tamano = len(matriz) # Asumimos que es cuadrada, tamano = M
    for i in range(tamano):
        # Diagonal Principal: elemento (i, i)
        matriz[i][i] = 0
        # Diagonal Secundaria: elemento (i, tamano - 1 - i)
        matriz[i][tamano - 1 - i] = 0

# --- Inicio de la ejecución principal del script ---
print("--- Programa: Ceros en Diagonales de Matriz Cuadrada ---")

tamano_m = obtener_tamano_matriz()

if tamano_m > 0:
    matriz_original = ingresar_elementos_matriz(tamano_m)
    imprimir_matriz(matriz_original, "Matriz Original Ingresada")

    poner_ceros_en_diagonales(matriz_original) # Modifica la matriz en su lugar
    imprimir_matriz(matriz_original, "Matriz Modificada con Ceros en Diagonales")
else:
    # El mensaje de tamaño inválido ya se da en obtener_tamano_matriz si es <=0 o no numérico
    # pero si obtener_tamano_matriz devolviera un código de error (ej. None o 0) lo manejaríamos aquí.
    # En este caso, si devuelve 0, no hacemos nada más.
    print("No se procesará ninguna matriz debido al tamaño inválido o cero.")

print("\n--- Fin del Programa ---") 