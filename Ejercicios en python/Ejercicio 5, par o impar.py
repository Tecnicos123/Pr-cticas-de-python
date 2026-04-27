# Crea un programa que determine si un número ingresado por el usuario es par o impar

number = int(input("Ingresa un número entero: "))
if number % 2 == 0:
    print(number, "es un número par.")
else:
    print(number, "es impar.")
