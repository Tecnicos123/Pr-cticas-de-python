# Las tuplas en Python son estructuras de datos ordenadas e inmutables (no se pueden modificar después de crearse). Se definen usando paréntesis () o simplemente separando elementos por comas.
# Creación de tuplas

# Diferentes formas de crear tuplas
tupla1 = (1, 2, 3, 4)
tupla2 = 1, 2, 3, 4  # Los paréntesis son opcionales
tupla3 = ("Python", "Java", "C++")
tupla4 = (1, "texto", 3.14, True)  # Pueden contener diferentes tipos
tupla_vacia = ()
tupla_un_elemento = (5,)  # Nota la coma para tuplas de un elemento

# Acceso a elementos
coordenadas = (10, 20, 30)
print(coordenadas[0])  # 10
print(coordenadas[-1])  # 30 (último elemento)
print(coordenadas[1:3])  # (20, 30) - slicing

# Usos comunes de las tuplas
# Coordenadas y puntos
punto_2d = (5, 10)
punto_3d = (1, 2, 3)
rectangulo = ((0, 0), (10, 5))  # esquina inferior izquierda y superior derecha

# Retorno múltiple de funciones
def obtener_nombre_edad():
    return "Ana", 25

nombre, edad = obtener_nombre_edad()  # Desempaquetado
print(f"{nombre} tiene {edad} años")

# Configuraciones inmutables
CONFIGURACION_DB = ("localhost", 5432, "mi_base_datos")
servidor, puerto, db = CONFIGURACION_DB

# Como claves en diccionarios
# Las tuplas pueden ser claves porque son inmutables
temperaturas = {
    (2024, 1): 15.5,   # enero 2024
    (2024, 2): 18.2,   # febrero 2024
    (2024, 3): 22.1    # marzo 2024
}

# Intercambio de variables
a = 10
b = 20
a, b = b, a  # Intercambio usando tuplas implícitas
print(f"a = {a}, b = {b}")  # a = 20, b = 10

# Datos relacionados
# Información de estudiantes
estudiantes = [
    ("María", 20, "Ingeniería"),
    ("Carlos", 22, "Medicina"),
    ("Ana", 19, "Derecho")
]

for nombre, edad, carrera in estudiantes:
    print(f"{nombre} ({edad} años) estudia {carrera}")

# Argumentos de funciones
def saludar(nombre, apellido, edad):
    return f"Hola {nombre} {apellido}, tienes {edad} años"

datos_persona = ("Juan", "Pérez", 30)
mensaje = saludar(*datos_persona)  # Desempaquetado con *

# Métodos útiles
numeros = (1, 2, 3, 2, 4, 2)
print(numeros.count(2))  # 3 - cuenta ocurrencias
print(numeros.index(3))  # 2 - índice de la primera ocurrencia
print(len(numeros))      # 6 - longitud

# Las tuplas son ideales cuando necesitas almacenar datos que no cambiarán durante la ejecución del programa, como coordenadas, configuraciones, o cuando quieres asegurar la integridad de los datos.