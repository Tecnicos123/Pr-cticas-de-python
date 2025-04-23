def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "No se puede dividir por cero"
    return x / y

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Suma: ", sumar(num1, num2))
print("Diferencia: ", restar(num1, num2))
print("Producto: ", multiplicar(num1, num2))
print("Cociente: ", dividir(num1, num2))