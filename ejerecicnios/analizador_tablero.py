def analizar_tablero(tablero):
    """
    Analiza un tablero de ajedrez representado por una matriz y cuenta
    fichas azules, posiciones vacías y el total de fichas.

    Args:
        tablero (list): Una lista de listas representando el tablero.
                        1 = ficha azul
                        2 = ficha roja
                        3 = posición vacía
    """
    num_fichas_azules = 0
    num_posiciones_vacias = 0
    num_fichas_rojas = 0  # Necesario para calcular el total de fichas

    # # Imprimir el tablero para visualización (opcional) - SE ELIMINA ESTA SECCIÓN
    # print("Tablero:")
    # for fila in tablero:
    #     # Imprimimos cada elemento de la fila con espacios entre ellos
    #     for i in range(len(fila)):
    #         print(fila[i], end="") # Imprime el número
    #         if i < len(fila) - 1:
    #             print(" ", end="") # Imprime un espacio si no es el último elemento
    #     print() # Nueva línea para la siguiente fila
    # print("\nAnálisis del Tablero:") # Se mantiene el título del análisis

    print("\nAnálisis del Tablero:") # Se añade un salto de línea si la impresión del tablero se elimina

    for fila in tablero:
        for celda in fila:
            if celda == 1:
                num_fichas_azules = num_fichas_azules + 1
            elif celda == 2:
                num_fichas_rojas = num_fichas_rojas + 1
            elif celda == 3:
                num_posiciones_vacias = num_posiciones_vacias + 1

    num_total_fichas = num_fichas_azules + num_fichas_rojas

    print(f"Número de fichas azules: {num_fichas_azules}")
    print(f"Número de posiciones vacías: {num_posiciones_vacias}")
    print(f"Número total de fichas: {num_total_fichas}")

def ingresar_tablero_usuario():
    """
    Permite al usuario ingresar las dimensiones y los valores del tablero.
    Retorna el tablero como una lista de listas.
    """
    print("\n--- Ingreso de datos del Tablero ---")
    num_filas = int(input("Ingrese el número de filas del tablero: "))
    num_columnas = int(input("Ingrese el número de columnas del tablero: "))

    tablero_nuevo = []
    for i in range(num_filas):
        fila_actual = []
        print(f"\n--- Fila {i + 1} ---")
        for j in range(num_columnas):
            # Se elimina la validación estricta. Cualquier entero es aceptado.
            # La lógica de conteo en analizar_tablero() se encargará de
            # interpretar solo los valores 1, 2 y 3.
            entrada_usuario = input(f"Ingrese valor para celda ({i + 1},{j + 1}): ")
            # Asumimos que el usuario ingresará un número entero.
            # No se incluye try-except para la conversión a int para mantener la simplicidad
            # según las reglas de desarrollo previas.
            valor_celda = int(entrada_usuario)
            fila_actual.append(valor_celda)
        tablero_nuevo.append(fila_actual)
    return tablero_nuevo

mi_tablero = ingresar_tablero_usuario()
analizar_tablero(mi_tablero)

    # Se eliminan los ejemplos de tableros predefinidos que estaban comentados 