import math

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

mcd = math.gcd(num1, num2)
print("El Máximo Común Divisor (MCD) de", num1, "y", num2, "es: ", mcd)

mcm = (num1 * num2) // mcd
print("El Mínimo Común Múltipo (MCM) de", num1, "y", num2, "es: ", mcm)