'''
Fuente: https://www.mclibre.org/consultar/python/lecciones/python-funciones-2.html
Escriba una función para obtener la media de dos números.
'''
def escribe_media():
    media = (a + b) / 2
    print(f"La media de {a} y {b} es {media}")
    return

a = 3
b = 5

escribe_media()
print("Programa terminado.")

'''
El problema de una función de este tipo es que es muy difícil de reutilizar en otros programas o incluso en el mismo programa, ya que sólo es capaz de hacer la media de las variables "a" y "b". Si en el programa no se utilizan esos nombres de variables, la función no funcionaría.

Para evitar ese problema, las funciones admiten argumentos, es decir, permiten que se les envíen valores con los que trabajar. De esa manera, las funciones se pueden reutilizar más fácilmente, como muestra el ejemplo siguiente:
'''
def escribe_media(x, y):
    media = (x + y) / 2
    print(f"La media de {x} y {y} es {media}")
    return

a = 3
b = 5

escribe_media(a, b)
print("Programa terminado.")

'''
Las funciones se pueden reutilizar más fácilmente, como muestra el ejemplo siguiente:
Ejemplo de función 3
'''

def calcula_media(x, y):
    resultado = (x + y) / 2
    return resultado

a = 3
b = 5
media = calcula_media(a, b)
print(f"La media de {a} y {b} es {media}")
print("Programa terminado.")

