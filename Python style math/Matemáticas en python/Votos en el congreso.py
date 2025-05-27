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

# Fin del programa

# Otro ejemplo de código que podría ser útil para resolver este caso y verificar la entrada del usuario:

print("Porcentaje de los parlamentarios")

while True:
    try:
        votos_favor_ley = int(input("Ingrese la cantidad de votos a favor de la ley: "))
        votos_encontra_ley = int(input("Ingrese la cantidad de votos en contra: "))
        votos_nulos = int(input("Ingrese la cantidad de votos nulos o abstenciones: "))

        total = votos_favor_ley + votos_encontra_ley + votos_nulos

        if total == 100:
            porcentaje_favor = votos_favor_ley / total * 100
            porcentaje_contra = votos_encontra_ley / total * 100
            porcentaje_nulos = votos_nulos / total * 100

            print(f"\nEl porcentaje de votos a favor fue de {porcentaje_favor:.2f}%")
            print(f"El porcentaje de votos en contra fue de {porcentaje_contra:.2f}%")
            print(f"El porcentaje de votos nulos o abstenciones fue de {porcentaje_nulos:.2f}%")
            break  # Salir del bucle si los datos son válidos

        else:
            print("Error: La suma total de votos debe ser exactamente 100. Intente nuevamente.\n")

    except ValueError:
        print("Error: Debes ingresar solo números enteros válidos. Intente nuevamente.\n")
# Fin del programa
# Este código permite ingresar la cantidad de votos a favor, en contra y nulos,
# y verifica que la suma total sea exactamente 100 antes de calcular los porcentajes.
# Si la suma no es 100, solicita al usuario que ingrese los datos nuevamente.

