'''
Diccionarios: Almacenan pares clave-valor, son mutables y no mantienen orden en versiones antiguas de Python.
Un diccionario es una colección de elementos que se accede mediante claves únicas.
Los diccionarios son útiles para almacenar datos relacionados y acceder a ellos de manera eficiente.

Ejemplos:
'''
mi_dict = {"nombre": "Juan", "edad": 25}
mi_dict["ciudad"] = "Madrid"  # Agregar nueva clave

print(mi_dict)  # Imprime: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}
print(mi_dict["nombre"])  # Imprime: Juan
print(mi_dict.get("edad"))  # Imprime: 25
print(mi_dict.keys())  # Imprime: dict_keys(['nombre', 'edad', 'ciudad'])

# Modificar un valor
mi_dict["edad"] = 26
print(mi_dict)  # Imprime: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Madrid'}   
# Eliminar una clave
del mi_dict["ciudad"]
print(mi_dict)  # Imprime: {'nombre': 'Juan', 'edad': 26}   
# Verificar si una clave existe
if "nombre" in mi_dict:
    print("La clave 'nombre' existe en el diccionario.")  # Imprime: La clave 'nombre' existe en el diccionario.    