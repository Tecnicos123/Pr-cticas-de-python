lista_de_diccionarios = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}, {'name': 'Bob', 'age': 35}]
lista_ordenada = sorted(lista_de_diccionarios, key=lambda x: x['age'])
print("Lista de diccionarios ordenada: ", lista_ordenada)