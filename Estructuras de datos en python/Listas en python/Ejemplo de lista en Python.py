# Una lista en Python es una estructura de datos que permite almacenar múltiples elementos en una secuencia ordenada. Los elementos pueden ser de diferentes tipos y se pueden modificar después de crear la lista.

# Ejemplo básico:

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Crear una lista de strings
frutas = ["manzana", "banana", "naranja"]

# Crear una lista mixta
mixta = [1, "hola", 3.14, True]

# Operaciones comunes con listas:

# Lista inicial
colores = ["rojo", "verde", "azul"]

# Agregar elementos
colores.append("amarillo")  # Agrega al final
colores.insert(1, "morado")  # Inserta en posición específica

# Acceder a elementos
primer_color = colores[0]  # "rojo"
ultimo_color = colores[-1]  # "amarillo"

# Modificar elementos
colores[0] = "rosa"

# Eliminar elementos
colores.remove("verde")  # Elimina por valor
elemento = colores.pop(1)  # Elimina por índice y retorna el elemento

# Longitud de la lista
cantidad = len(colores)

print(colores)  # Resultado: ['rosa', 'azul', 'amarillo']

