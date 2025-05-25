# En el congreso se vota la sanción a una nueva ley
# Desarrolla un programa que permita ingresar la cantidad
# de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.

print("Porcentaje de los parlamentarios")
votos_favor_ley = int(input("Ingrese la cantidad de votos a favor de la ley: "))
votos_encontra_ley = int(input("Ingrese la cantidad de votos en contra: "))

total = votos_favor_ley + votos_encontra_ley

if total > 0:
    porcentaje_favor = votos_favor_ley / total * 100
    porcentaje_contra = votos_encontra_ley / total * 100
    
    print(f"El porcentaje de votos a favor fue de {porcentaje_favor:.2f}%")
    print(f"El porcentaje de votos en contra fue de {porcentaje_contra:.2f}%")
else:
    print("No hay votos registrados")