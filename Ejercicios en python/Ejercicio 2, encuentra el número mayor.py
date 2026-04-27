# Ejercicio No 2, encuentra el número mayor
# Saca el número mayor de dos números ingresados por el usaurio.

number1 = float(input("Enter de first number: "))
number2 = float(input("Enter the second number: "))
if number1 > number2:
    print("El número mayor es: ", number1)
elif number1 < number2:
    print("El número mayor es: ", number2)
else:
    print("They are the same")