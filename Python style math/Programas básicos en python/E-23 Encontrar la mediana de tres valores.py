def encontrar_mediana(a, b, c):
    return sorted([a, b, c])[1]

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el seguno número: "))
num3 = float(input("Ingrese el tercer número: "))

print("Mediana: ", encontrar_mediana(num1, num2, num3))