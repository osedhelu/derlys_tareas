def ingresar_cuadrado():
   
    cuadrado = []
    print("Ingrese los números para el cuadrado (del 1 al 9):")
    for i in range(3):
        fila_actual = []
        i_mas_uno = i + 1
        print("Fila", i_mas_uno, ":")
        for j in range(3):
            while True:
                j_mas_uno = j + 1
                mensaje_input = "  Ingrese el número para la columna " + str(j_mas_uno) + ": "
                numero_str = input(mensaje_input)
                valor_ingresado = int(numero_str)

                if valor_ingresado >= 1 and valor_ingresado <= 9:
                    fila_actual.append(valor_ingresado)
                    break
                else:
                    mensaje_error = "Número inválido. Debe estar entre 1 y 9. Intente de nuevo."
                    print(mensaje_error)
        cuadrado.append(fila_actual)
    return cuadrado

def es_magico(cuadrado):
    suma_referencia = 0
    longitud_fila_0 = len(cuadrado[0])
    for k_idx in range(longitud_fila_0):
        suma_referencia = suma_referencia + cuadrado[0][k_idx]

    longitud_cuadrado = len(cuadrado) 
    for i in range(longitud_cuadrado):
        suma_fila_actual = 0
        longitud_fila_i = len(cuadrado[i]) 
        for j in range(longitud_fila_i):
            suma_fila_actual = suma_fila_actual + cuadrado[i][j]
        if suma_fila_actual != suma_referencia:
            return False

    num_columnas = len(cuadrado[0]) 
    for j in range(num_columnas):
        suma_columna_actual = 0
        for i in range(longitud_cuadrado):
            suma_columna_actual = suma_columna_actual + cuadrado[i][j]
        if suma_columna_actual != suma_referencia:
            return False
        
    suma_diag_principal = 0
    for i in range(longitud_cuadrado): 
        suma_diag_principal = suma_diag_principal + cuadrado[i][i]
    if suma_diag_principal != suma_referencia:
        return False

    
    suma_diag_secundaria = 0
    indice_base_diag_sec = longitud_cuadrado - 1
    for i in range(longitud_cuadrado):
        suma_diag_secundaria = suma_diag_secundaria + cuadrado[i][indice_base_diag_sec - i]
    if suma_diag_secundaria != suma_referencia:
        return False
    return True

mi_cuadrado = ingresar_cuadrado()

print("\nCuadrado ingresado:") 
longitud_mi_cuadrado = len(mi_cuadrado)
for i in range(longitud_mi_cuadrado):
    longitud_fila_actual = len(mi_cuadrado[i])
    for j in range(longitud_fila_actual):
        print(str(mi_cuadrado[i][j]), end=" ") 
    print()

if es_magico(mi_cuadrado):
    print("\n¡El cuadrado es mágico!")
else:
    print("\nEl cuadrado NO es mágico.")