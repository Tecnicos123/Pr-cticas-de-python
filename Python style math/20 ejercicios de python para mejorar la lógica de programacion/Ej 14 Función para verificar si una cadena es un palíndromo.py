cadena = input("Introdece una cadena de texto: ")

reversa = cadena [::-1]

if cadena.lower() == reversa.lower():
    print(f"{cadena} es un palíndromo")
else:
    print(f"{cadena} no es un palíndromo")