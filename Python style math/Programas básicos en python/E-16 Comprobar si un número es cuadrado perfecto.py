import math

def es_cuadrado_perfecto(n):
    raiz = math.isqrt(n)
    return raiz * raiz == n

numero = int(input("Ingrese un número: "))
if es_cuadrado_perfecto(numero):
    print("Cuadrado perfecto")
else:
    print("No es un cuadrado perfecto")
