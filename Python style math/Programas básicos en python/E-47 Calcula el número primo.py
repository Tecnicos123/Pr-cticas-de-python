def es_primo(x):
    if x <= 1:  # Agregué esta validación para números menores o iguales a 1
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

def generar_primo(primo_actual):
    nuevo_primo = primo_actual + 1
    while not es_primo(nuevo_primo):
        nuevo_primo += 1
    return nuevo_primo  # Esta línea estaba mal indentada dentro del ciclo while

def main():
    primo_actual = 2
    while True:
        respuesta = input('¿Desea ver el siguiente número primo? (S/N) ')
        if respuesta.lower().startswith('s'):
            print(primo_actual)
            primo_actual = generar_primo(primo_actual)
        else:
            break  # Esta línea estaba mal indentada

if __name__ == '__main__':  # Corregí la sintaxis con los guiones bajos
    main()

kilometros = float(input("Ingrese la distancia en kilómetros: "))

factor_de_conversion = 0.621371

millas = kilometros * factor_de_conversion
print(f"{kilometros} kilómetros es igual a {millas} millas")