# Se desea conocer el precio de un boleto de viaje en tren
# hay un valor fijo mas un valor extra calculado en base a la cantidad de kilómetros (klm) a recorrer.
# Por cada klm a recorrer se cobra B/0.30 adicional

adicional_klm = 0.30

print("Costo del boleto de viaje")

costo_base = float(input("Ingrese el costo del boleto: "))

klm = int(input("Ingrese los klm a recorrer: "))

adicional = klm * adicional_klm
costo_total = costo_base + adicional

print("El costo del viaje es:", costo_total)