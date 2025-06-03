def ingresar_datos_produccion(num_vacas):
    """
    Permite al usuario ingresar la producción de leche diaria para cada vaca durante una semana.
    Args:
        num_vacas (int): El número total de vacas en el hato.
    Returns:
        list: Una matriz (lista de listas) con la producción semanal.
              Filas representan vacas, columnas representan días (0-6).
    """
    produccion_semanal = []
    dias_semana = 7

    for i in range(num_vacas):
        produccion_vaca_actual = []
        print(f"\n--- Vaca número {i + 1} ---")
        for j in range(dias_semana):
            # Se usa un bucle para asegurar que la entrada sea un número positivo
            produccion_dia = -1.0
            while produccion_dia < 0:
                entrada_usuario = input(f"  Ingrese producción para el día {j + 1} (litros): ")
                # Asumimos que el usuario ingresará un número, como en ejercicios anteriores.
                # Se permite float para litros.
                # No se incluye try-except complejo para mantener simplicidad de reglas.
                # Si la entrada no es un número, podría dar error. Una solución simple sería
                # pedir que se reintente, pero eso añade complejidad no pedida.
                # Por ahora, se confía en la entrada numérica.
                # El valor se convierte a float.
                val_temp = float(entrada_usuario) 
                if val_temp >= 0:
                    produccion_dia = val_temp
                else:
                    print("  La producción no puede ser negativa. Intente de nuevo.")
            produccion_vaca_actual.append(produccion_dia)
        produccion_semanal.append(produccion_vaca_actual)
    return produccion_semanal

def analizar_y_mostrar_resultados(produccion_semanal, num_vacas):
    """
    Analiza la producción semanal y muestra los resultados solicitados.
    Args:
        produccion_semanal (list): Matriz con la producción.
        num_vacas (int): Número de vacas.
    """
    dias_semana = 7

    print("\n--- Resultados Producción Lechera ---")

    # 1. Producción total del hato en cada uno de los siete días.
    print("\n1. Producción total del hato por día:")
    for j in range(dias_semana):
        total_leche_dia = 0.0
        for i in range(num_vacas):
            total_leche_dia = total_leche_dia + produccion_semanal[i][j]
        print(f"  Día {j + 1}: {total_leche_dia} litros")

    # 2. El número de la vaca que dio más leche en cada día.
    print("\n2. Vaca con mayor producción por día:")
    if num_vacas > 0:
        for j in range(dias_semana):
            max_leche_este_dia = -1.0 
            vaca_lider_este_dia = 0 # Guardará el número 1-indexado de la vaca
            
            # Inicializar con la primera vaca si existen vacas
            if num_vacas > 0:
                 max_leche_este_dia = produccion_semanal[0][j]
                 vaca_lider_este_dia = 1

            for i in range(num_vacas): # i es el índice 0-indexado de la vaca
                if produccion_semanal[i][j] > max_leche_este_dia:
                    max_leche_este_dia = produccion_semanal[i][j]
                    vaca_lider_este_dia = i + 1 # Convertir a número de vaca 1-indexado
            print(f"  Día {j + 1}: Vaca número {vaca_lider_este_dia} (con {max_leche_este_dia} litros)")
    else:
        print("  No hay datos de vacas para analizar.")

    # 3. La mayor producción de leche obtenida en un día (por cualquier vaca).
    print("\n3.  ")
    mayor_produccion_individual_global = -1.0
    if num_vacas > 0:
        # Inicializar con la producción de la primera vaca el primer día
        mayor_produccion_individual_global = produccion_semanal[0][0]
        for i in range(num_vacas):
            for j in range(dias_semana):
                if produccion_semanal[i][j] > mayor_produccion_individual_global:
                    mayor_produccion_individual_global = produccion_semanal[i][j]
        print(f"  La mayor producción individual en un día fue: {mayor_produccion_individual_global} litros")
    else:
        print("  No hay datos de producción para analizar.")


print("--- Control  de la Hacienda ---")

num_total_vacas = -1
while num_total_vacas < 0: # Pedir hasta que sea 0 o más. Si es 0, se manejará después.
    entrada_n_vacas = input("Ingrese el número total de vacas en el hato: ")
    # Se asume que se ingresa un entero.
    num_total_vacas = int(entrada_n_vacas)
    if num_total_vacas < 0:
        print("El número de vacas no puede ser negativo. Intente de nuevo.")

if num_total_vacas == 0:
    print("No hay vacas en el hato para registrar producción.")
else:
    print(f"Se registrará la producción para {num_total_vacas} vaca(s).")
    matriz_produccion = ingresar_datos_produccion(num_total_vacas)
    analizar_y_mostrar_resultados(matriz_produccion, num_total_vacas)
