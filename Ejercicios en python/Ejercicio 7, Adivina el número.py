# Adivina el número

import random

# Genera un número aleatorio entre 1 al 50

numero_secreto = random.randint(1, 50)

intentos = 0
adivinado = False

print("¡Adivina el número secreto entre 1 al 50!")

while not adivinado:
    try:
        # Pide al usuario que ingrese un número
        guess = int(input("Ingrese un número: "))
        intentos += 1
        
        # Compara el número ingresado con el número secreto
        if guess == numero_secreto:
            adivinado = True
        elif guess < numero_secreto:
            print("El número es mayor, intenta de nuevo.")
        else:
            print("El número es menor, intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
        
# Cuando el usuario adivina el número
print(f"¡Felicitaciones!, Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
      