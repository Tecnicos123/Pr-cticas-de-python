#contar el número de vocales

vocales = "aeiouAEIOU"

cadena = input("Introduce una cadena de texto: ")

contador_vocales = 0

for letra in cadena:
    if letra in vocales:
        contador_vocales += 1
        
print(f"El número de vocales en la cadena es: {contador_vocales}")