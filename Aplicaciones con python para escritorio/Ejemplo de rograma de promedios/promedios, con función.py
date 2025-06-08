'''
Ahora calculamos el mismo promedio, pero con una función:

Componentes de una función:
1. Palabra clave def: Indica que estás definiendo una función
2. Nombre de la función: Debe seguir las reglas de nomenclatura de Python (sin espacios, puede contener letras, números y guiones bajos)
3. Parámetros: Van entre paréntesis, separados por comas. Pueden ser opcionales
4. Dos puntos (:): Marcan el inicio del bloque de código
5. Cuerpo de la función: Código indentado que se ejecuta cuando llamas la función
6. return: Opcional, devuelve un valor al código que llamó la función

Ejemplo de programa de promedios con función
Este programa calcula el promedio de dos notas utilizando una función
Puedes usar este código como base para crear programas más complejos
o para aprender más sobre funciones en Python.

'''

def promedio(nota_1, nota_2):
    promedio = (nota_1 + nota_2)/2
    return promedio

resultado1 = promedio(4.3, 3.5)
print("El promedio es:", resultado1)
