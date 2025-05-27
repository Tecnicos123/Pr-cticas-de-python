# Verificar si un número es positivo o negativo

def verificar_numero():
    while True:
        entrada = input("Ingresa un número: ")
        
        try:
            numero = float(entrada)
            
            if numero > 0:
                print("El número es positivo.")
            elif numero < 0:
                print("El número es negativo.")
            else:
                print("El número es cero.")
            
            break  # Salir del bucle si la entrada es válida
        
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta nuevamente.")

# Ejecutar la función
verificar_numero()


