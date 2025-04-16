#crear una función que devuelva el cuadrado de un número

def cuadrado_num(num):
    return num ** 2

num = int(input("Introduce un número para calcular su cuadrado: "))

print(f"El cuadrado de {num} es {cuadrado_num(num)}")