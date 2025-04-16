#crear una lista de números y calcular la suma

num = int(input("Introduce el número final de la lista: "))

lista = list(range(1, num +1))

resultado = sum(lista)

print(f"La suma de la lista hasta {num} es {resultado}")