# Precio de venta
# Conociendo el precio de lista de un artículo, determinar:
# Precio de venta al contado (10% de descuento)
# Precio de venta a crédito (5% de recargo)

print("Precio de venta")

lista = float(input("Ingrese el precio de lista del artículo: "))

contado = lista - (lista * 10 / 100)
credito = lista + (lista * 5 / 100)

print(f"Precio al contado B/ {contado:.2f}")
print(f"Precio al crédito B/ {credito:.2f}")

