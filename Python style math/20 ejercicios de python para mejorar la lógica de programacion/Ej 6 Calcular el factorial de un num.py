#calcular el factorial de un número usando un bucle while

#solicita el número al usuario

num = int(input("Introduce un número: "))

#Inicializar variables
factorial = 1
i = 1

#Usar un bucle while para calcular el factorial
while i <= num:
    factorial *= i
    i += 1
    
#mostrar el resultado
print(f"El factorial de {num} es {factorial}")