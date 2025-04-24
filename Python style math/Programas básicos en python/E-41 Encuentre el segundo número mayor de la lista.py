numeros = [30, 10, 45, 5, 20]

numeros.sort(reverse=True)

if len(numeros) >= 2:
    segundo_mayor = numeros[1]
    print("El segundo número más grande en la lista es: ", segundo_mayor)
else:
    print("La lista no contiene un segundo número mas grande.")