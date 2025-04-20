def es_numero_perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n

numero = int(input("Ingrese un número: "))
if es_numero_perfecto(numero):
    print("Número perfecto")
else:
    print("No es un número perfecto")