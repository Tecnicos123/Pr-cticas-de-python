'''
Los conjuntos (sets) en Python son estructuras de datos muy útiles para almacenar elementos únicos y realizar operaciones matemáticas entre ellos. Te muestro los principales ejemplos y usos:

Este código cubre la creación de conjuntos, operaciones básicas, casos de uso prácticos y ejemplos de conjuntos inmutables (frozenset).

'''
# Ejemplos de Conjuntos

# Conjunto vacío
conjunto_vacio = set()

# Conjunto con elementos
numeros = {1, 2, 3, 4, 5}
frutas = {"manzana", "banana", "naranja"}

# Desde una lista (elimina duplicados automáticamente)
lista = [1, 2, 2, 3, 3, 4]
conjunto_desde_lista = set(lista)  # {1, 2, 3, 4}

# Operaciones básicas con conjuntos
frutas = {"manzana", "banana", "naranja"}

# Agregar elementos
frutas.add("uva")
frutas.update(["kiwi", "mango"])  # Agregar múltiples

# Eliminar elementos
frutas.remove("banana")  # Error si no existe
frutas.discard("pera")   # No error si no existe
elemento = frutas.pop()  # Elimina y retorna elemento aleatorio

# Verificar pertenencia
print("manzana" in frutas)  # True
print(len(frutas))          # Tamaño del conjunto

# Operaciones matemáticas
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Unión
union = set_a | set_b           # {1, 2, 3, 4, 5, 6, 7, 8}
union = set_a.union(set_b)      # Método alternativo

# Intersección
interseccion = set_a & set_b    # {4, 5}
interseccion = set_a.intersection(set_b)

# Diferencia
diferencia = set_a - set_b      # {1, 2, 3}
diferencia = set_a.difference(set_b)

# Diferencia simétrica
sim_diff = set_a ^ set_b        # {1, 2, 3, 6, 7, 8}
sim_diff = set_a.symmetric_difference(set_b)

# Casos de Uso Prácticos
# 1 - Eliminar Duplicados

# De una lista
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4]
sin_duplicados = list(set(lista_con_duplicados))

# De un string
texto = "programming"
letras_unicas = set(texto)  # {'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n'}

# 2 - Verificación de Membresía Rápida

usuarios_premium = {"juan", "ana", "carlos", "lucia"}

def es_premium(usuario):
    return usuario in usuarios_premium  # O(1) muy eficiente

print(es_premium("ana"))    # True
print(es_premium("pedro"))  # False

# 3 - Comparar Listas de Elementos

estudiantes_matematicas = {"ana", "juan", "pedro", "lucia"}
estudiantes_fisica = {"juan", "carlos", "lucia", "maria"}

# Estudiantes en ambas materias
ambas = estudiantes_matematicas & estudiantes_fisica  # {"juan", "lucia"}

# Solo en matemáticas
solo_mate = estudiantes_matematicas - estudiantes_fisica  # {"ana", "pedro"}

# En cualquiera de las dos
cualquiera = estudiantes_matematicas | estudiantes_fisica

# 4 - Filtrado y Procesamiento de Datos

# Encontrar elementos comunes entre múltiples listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
lista3 = [4, 5, 6, 7, 8]

comunes = set(lista1) & set(lista2) & set(lista3)  # {4, 5}

# Validar que todos los elementos requeridos están presentes
elementos_requeridos = {"nombre", "email", "edad"}
datos_usuario = {"nombre": "Juan", "email": "juan@email.com", "telefono": "123"}

campos_faltantes = elementos_requeridos - set(datos_usuario.keys())
if campos_faltantes:
    print(f"Faltan campos: {campos_faltantes}")

# 5 - Análisis de Texto

def palabras_unicas(texto):
    palabras = texto.lower().split()
    return set(palabras)

def palabras_comunes(texto1, texto2):
    set1 = set(texto1.lower().split())
    set2 = set(texto2.lower().split())
    return set1 & set2

texto_a = "Python es un lenguaje de programación"
texto_b = "Java es otro lenguaje de programación"

comunes = palabras_comunes(texto_a, texto_b)  # {"es", "de", "lenguaje", "programación"}

# Frozenset (Conjuntos Inmutables)

# Para cuando necesitas un conjunto que no cambie
conjunto_inmutable = frozenset([1, 2, 3, 4])

# Útil como clave en diccionarios
diccionario = {
    frozenset([1, 2]): "grupo_a",
    frozenset([3, 4]): "grupo_b"
}

'''
Los conjuntos son especialmente útiles cuando necesitas eliminar duplicados, realizar operaciones de teoría de conjuntos, o cuando la velocidad de búsqueda es importante (la verificación de pertenencia es O(1) en promedio).
'''
# Ejemplo de uso de conjuntos en un programa
def main():
    # Crear un conjunto de frutas
    frutas = {"manzana", "banana", "naranja"}
    
    # Agregar una fruta
    frutas.add("uva")
    
    # Verificar si una fruta está en el conjunto
    if "manzana" in frutas:
        print("La manzana está en el conjunto.")
    
    # Mostrar todas las frutas
    print("Frutas:", frutas)
    
    # Realizar una operación de unión con otro conjunto
    otras_frutas = {"kiwi", "mango"}
    todas_frutas = frutas | otras_frutas
    print("Todas las frutas:", todas_frutas)

if __name__ == "__main__":
    main()
# Este programa crea un conjunto de frutas, agrega una fruta, verifica la pertenencia de una fruta y muestra todas las frutas, incluyendo una unión con otro conjunto de frutas.
# Puedes ejecutar este código para ver cómo funcionan los conjuntos en Python.
# Recuerda que los conjuntos no mantienen un orden específico, por lo que al imprimirlos, el orden puede variar.
# Además, los conjuntos no permiten elementos duplicados, lo que los hace ideales para almacenar colecciones únicas de elementos.