# Convertir grados Fahrenheit a grados Celsius
# Fórmula: C = (F - 32) / 1.8

F = input("Ingrese un valor: ")
C = round((int(F)-32)/1.8)

print("C: ",C)

# Convertir grados Celsius a grados Fahrenheit con una función

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

# Solicitar al usuario el valor en Fahrenheit
fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))

# Convertir y mostrar el resultado
celsius = fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius:.2f} grados Celsius.")
