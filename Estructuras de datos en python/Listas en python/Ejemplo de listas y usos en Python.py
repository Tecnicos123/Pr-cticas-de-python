# Diferentes tipos de listas en Python y sus usos más comunes:
# Listas basicas, listas de números, listas de strings y listas mixtas.

# Lista de números
numeros = [1, 2, 3, 4, 5]
print(numeros)  # [1, 2, 3, 4, 5]

# Lista de strings
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])  # manzana

# Lista mixta
mixta = [1, "hola", 3.14, True]
print(mixta)  # [1, 'hola', 3.14, True]

# Operaciones comunes

# Agregar elementos
frutas.append("uva")  # Al final
frutas.insert(1, "pera")  # En posición específica

# Eliminar elementos
frutas.remove("banana")  # Por valor
elemento = frutas.pop()  # Elimina y retorna el último
del frutas[0]  # Por índice

# Acceder a elementos
print(frutas[0])      # Primer elemento
print(frutas[-1])     # Último elemento
print(frutas[1:3])    # Slice: elementos del 1 al 2

# Recorrer listas
for fruta in frutas:
    print(fruta)

# Longitud de la lista
print(len(frutas))  # Número de elementos en la lista

# Comprobar existencia de un elemento
if "manzana" in frutas:
    print("La lista contiene manzana")

# Ordenar una lista 
frutas.sort()  # Ordena la lista alfabéticamente
print(frutas)  # Lista ordenada 

# Invertir una lista
frutas.reverse()  # Invierte el orden de la lista
print(frutas)  # Lista invertida

# Copiar una lista
frutas_copia = frutas.copy()  # Crea una copia de la lista
print(frutas_copia)  # Copia de la lista original

# Concatenar listas
otra_lista = ["kiwi", "piña"]
lista_concatenada = frutas + otra_lista  # Combina dos listas
print(lista_concatenada)  # Lista concatenada

# Listas anidadas
listas_anidadas = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(listas_anidadas[0])  # Primer sublista: [1, 2, 3]
print(listas_anidadas[1][2])  # Acceso a un elemento específico: 'c'

# Comprensión de listas
cuadrados = [x**2 for x in range(10)]  # Lista de cuadrados de 0 a 9
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]   

# Filtrar listas
pares = [x for x in range(20) if x % 2 == 0]  # Lista de números pares del 0 al 19
print(pares)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Mapear listas
dobles = list(map(lambda x: x * 2, numeros))  # Multiplica cada elemento por 2
print(dobles)  # [2, 4, 6, 8, 10]

# Reducir listas
from functools import reduce
suma_total = reduce(lambda x, y: x + y, numeros)  # Suma todos los elementos
print(suma_total)  # 15 

# Comprobar si una lista está vacía

if not frutas:
    print("La lista de frutas está vacía")
else:
    print("La lista de frutas tiene elementos")

# Convertir una cadena en una lista
cadena = "Python es genial"
lista_cadena = cadena.split()  # Divide la cadena en palabras
print(lista_cadena)  # ['Python', 'es', 'genial']

# Unir una lista en una cadena
lista_unida = " ".join(lista_cadena)  # Une las palabras con espacios
print(lista_unida)  # Python es genial

# Buscar el índice de un elemento
indice = frutas.index("manzana") if "manzana" in frutas else -1  # Índice de 'manzana'
print(indice)  # Índice de 'manzana' o -1 si no está

# Reemplazar un elemento en una lista
if "uva" in frutas:
    frutas[frutas.index("uva")] = "uva roja"  # Reemplaza 'uva' por 'uva roja'
print(frutas)  # Lista con 'uva' reemplazada por 'uva roja'

# Comprobar si dos listas son iguales
otra_fruta = ["pera", "manzana", "uva roja"]
if frutas == otra_fruta:
    print("Las listas son iguales")
else:
    print("Las listas son diferentes")  
        
# Crear una lista de listas     
listas_de_frutas = [["manzana", "pera"], ["banana", "naranja"], ["uva", "kiwi"]]
print(listas_de_frutas)  # Lista de listas de frutas    

# Acceder a un elemento en una lista de listas
print(listas_de_frutas[0][1])  # Accede a 'pera' en la primera sublista

# Usos prácticos: Almacenar datos de estudiantes

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Luis", "edad": 22, "calificacion": 92},
    {"nombre": "María", "edad": 19, "calificacion": 78}
]

# Encontrar estudiante con mejor calificación
mejor = max(estudiantes, key=lambda x: x["calificacion"])
print(f"Mejor estudiante: {mejor['nombre']}")

# Procesamiento de datos numéricos
ventas = [1500, 2300, 1800, 2100, 1900]

# Estadísticas básicas
total = sum(ventas)
promedio = total / len(ventas)
maximo = max(ventas)
minimo = min(ventas)

print(f"Total: {total}, Promedio: {promedio:.2f}")

# Manejo de inventarios
inventario = [
    {"producto": "laptop", "cantidad": 15, "precio": 800},
    {"producto": "mouse", "cantidad": 50, "precio": 25},
    {"producto": "teclado", "cantidad": 30, "precio": 45}
]

# Productos con stock bajo
stock_bajo = [item for item in inventario if item["cantidad"] < 20]
print("Productos con stock bajo:", [p["producto"] for p in stock_bajo])

# Listas anidadas (matrices)
# Tabla de multiplicar
tabla = [[i * j for j in range(1, 6)] for i in range(1, 6)]

# Imprimir tabla
for fila in tabla:
    print(fila)

# Acceder a elemento específico
print(tabla[2][3])  # Fila 2, columna 3

# Cola y pila
# Como cola (FIFO)
cola = []
cola.append("cliente1")  # Agregar al final
cola.append("cliente2")
siguiente = cola.pop(0)  # Quitar del inicio

# Como pila (LIFO)
pila = []
pila.append("tarea1")   # Agregar al final
pila.append("tarea2")
ultima = pila.pop()     # Quitar del final

# Métodos útiles
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# Ordenar
numeros.sort()          # Modifica la lista original
ordenados = sorted(numeros)  # Crea nueva lista

# Contar elementos
print(numeros.count(1))  # Cuenta cuántas veces aparece 1

# Encontrar índice
print(numeros.index(4))  # Índice del primer 4

# Invertir
numeros.reverse()       # Modifica la original
invertidos = numeros[::-1]  # Crea nueva lista invertida

# Limpiar
numeros.clear()         # Vacía la lista

# Las listas son extremadamente versátiles y son una de las estructuras de datos más utilizadas en Python por su flexibilidad y facilidad de uso.RetryClaude does not have the ability to run the code it generates yet.Claude can make mistakes. Please double-check responses.