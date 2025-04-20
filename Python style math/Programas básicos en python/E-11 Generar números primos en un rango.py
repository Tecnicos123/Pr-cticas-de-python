def generar_primos(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primos.append(num)
    return primos

inicio_rango = int(input("Ingrese el rango inicial: "))
fin_rango = int(input("Ingrese el rango final: "))

print("Números primos: ", generar_primos(inicio_rango, fin_rango))
