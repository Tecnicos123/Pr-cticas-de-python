"""
Ejercicio 6: Factorial

Escribe un programa que calcule el factorial de un número entero positivo ingresado
por el usuario.

Pista: ¿Qué es el factorial de un número? Es el producto de todos los números positivos
desde el 1 hasta el número en cuestión. Por ejemplo el factorial de 5 es: 1x2x3x4x5=120

"""

n = int(input("Ingresa un número entero positivo: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("El factorial de", n, "es:", factorial)