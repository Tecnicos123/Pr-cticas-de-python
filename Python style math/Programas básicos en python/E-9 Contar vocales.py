def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0

    for char in cadena:
        if char in vocales:
            contador += 1
    return contador
cadena = input("Ingrese una cadena: ")

print("Número de vocales: ", contar_vocales(cadena))
