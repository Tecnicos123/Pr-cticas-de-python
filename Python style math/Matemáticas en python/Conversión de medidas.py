# Conversión de Medidas.

# Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:
# yardas, pulgadas, centímetros y metros
# Sabiendo que:  1 pie = 12 pulgadas
#                1 yarda = 3 pies
#                1 pulgada = 2.54 centímetros
#                1 metro = 100 centímetros

print("Conversión de distancias")
pies = float(input("Ingrese las distancias en pies que desea convertir: "))

yardas = pies / 3
pulgadas = pies * 12
centimetros = pulgadas * 2.54
metros = centimetros / 100

print("En ", pies, " pies hay ", yardas, " yardas ")
print("En ", pies, " pies hay ", pulgadas, " pulgadas ")
print("En ", pies, " pies hay ", centimetros, " centimetros ")
print("En ", pies, " pies hay ", metros, " metros ")