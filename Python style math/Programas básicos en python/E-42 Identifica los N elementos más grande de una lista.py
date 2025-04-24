def encontrar_n_elementos_mas_grandes(lista, n):
    lista_ordenada = sorted(lista, reverse=True)
    elementos_mas_grandes = lista_ordenada[:n]
    return elementos_mas_grandes

numeros = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]

N = int(input("N = "))

resultado = encontrar_n_elementos_mas_grandes(numeros, N)
print(f"Los {N} elementos más grandes es la lista son: ", resultado)