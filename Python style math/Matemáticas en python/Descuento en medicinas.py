# Calcular el monto a pagar por medicamentos que tienen un
# descuento de 35%

print("Calculo de descuento en medicamentos")

precio_actual = float(input("Ingrese el precio actual: "))

descuento = precio_actual * 0.35

precio_nuevo = precio_actual - descuento

print("Precio original B/", precio_actual)
print("Descuento del 35%: B/", descuento)
print("Nuevo precio B/", precio_nuevo)