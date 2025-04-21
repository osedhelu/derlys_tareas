# Programa para calcular comisiones de vendedores

# Lista predefinida de ventas de ejemplo (en pesos)
ventas = [450000, 600000, 900000, 300000, 750000]

# Calcular comisiones
comisiones = []
for venta in ventas:
    if venta < 500000:
        comision = venta * 0.05  # 5%
    elif venta <= 800000:
        comision = venta * 0.08  # 8%
    else:
        comision = venta * 0.10  # 10%
    comisiones.append(comision)

# Calcular promedio de comisiones
promedio_comision = 0
for comision in comisiones:
    promedio_comision = promedio_comision + comision
promedio_comision = promedio_comision / len(comisiones)

# Contar vendedores con comisión mayor al promedio
vendedores_sobre_promedio = 0
ventas_sobre_promedio = 0

for i in range(len(comisiones)):
    if comisiones[i] > promedio_comision:
        vendedores_sobre_promedio = vendedores_sobre_promedio + 1
        ventas_sobre_promedio = ventas_sobre_promedio + ventas[i]

# Imprimir resultados
print("\nComisiones por vendedor:")
for i in range(len(comisiones)):
    print(f"Vendedor {i+1}: ${comisiones[i]:,.2f}")

print(f"\nPromedio de comisión de la tienda: ${promedio_comision:,.2f}")
print(f"Número de vendedores con comisión mayor al promedio: {vendedores_sobre_promedio}")
print(f"Total de ventas de vendedores con comisión mayor al promedio: ${ventas_sobre_promedio:,.2f}") 