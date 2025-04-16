#crear lista de números pares usando un bucle

lista_pares = []

for num in range(1, 31):
    if num % 2 == 0:
        lista_pares.append(num)
        
print (lista_pares)