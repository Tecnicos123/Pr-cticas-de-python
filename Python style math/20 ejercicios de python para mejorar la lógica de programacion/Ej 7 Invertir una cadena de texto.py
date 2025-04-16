#invertir una cadena de texto usando un bucle
#solicitar una cadena de texto al usuario

cadena = input("Introduce una cadena de texto: ")

reversa = ""

for letra in cadena:
    reversa = letra + reversa
    
print(f"La cadena invertida es: {reversa}")
