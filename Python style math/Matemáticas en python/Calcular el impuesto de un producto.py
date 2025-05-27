# Calcular el impuesto de un producto
# Fórmula: impuesto = precio * porcentaje_impuesto

cantidad = int(input("Ingrese la cantidad del producto: "))
precio = float(input("Ingrese el precio del producto: "))
subtotal = cantidad * precio
porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto (en %): "))
impuesto = (precio * porcentaje_impuesto) / 100

total = cantidad * (precio + impuesto)
print(f"El impuesto por cada producto es: {impuesto:.2f}")

print(f"El subtotal es: {subtotal:.2f}")
print(f"El total con impuesto es: {total:.2f}")
