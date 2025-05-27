# Un productor agrícola desea saber cuentos quintales de trigo puede producir en su parcela.
# Crear un programa que permita ingresar el largo y el ancho en metros de la parcela.
# Determinar si en 10 m^2 se obtiene 2 quintales

largo = int(input("Ingrese el largo de la parcela: "))
ancho = int(input("Ingrese el ancho de la parcela: "))

superficie = largo * ancho
rinde = (superficie * 2) // 10

print("El rendimiento que obtiene el productor en ", superficie, "metros cuadrados.")
print(" es de ", rinde, "quintales")