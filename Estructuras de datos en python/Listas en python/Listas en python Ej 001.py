# Estructuras de Datos en Python
# Definicióm: es una forma particular de organizar datos en una computadora para que puedan ser utilizados de manera eficiente. Diferentes tipos de estructuras de datos son adecuados para diferentes tipos de aplicaciones, y algunos son altamente especializados para tareas específicas.

# Listas: es una colección de elementos en un orden en particular.
# Fuente: https://jahazielponce.com/estructuras-de-datos-en-python/

# Ejercicio: 

# Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.

# A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

# Recorrer la lista para imprimir la sumatoria de todos los elementos.

# Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

# Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

import time
from typing import List


class Numeros(object):
    def __init__(self, lista_numeros: List[float]):
        self.lista_numeros = lista_numeros

    def __str__(self):
        res = f"{self.lista_numeros}"
        return res

    @staticmethod
    def valida_numero(numero_string: str):
        ''' Valida si un numero es correcto '''
        numero = None
        try:
            numero = float(numero_string)
        except:
            print(f"{numero_string} no es un numero valido, inténtalo de nuevo")
        return numero

    def suma(self):
        ''' Suma los elementos de la lista '''
        print(f"Suma: {sum(self.lista_numeros)}")

    def get_menores(self, numero):
        ''' Muestra los elementos menores a un numero '''
        print(f"Menores a {numero}")
        lista_menores = [x for x in self.lista_numeros if x < numero]
        if len(lista_menores) > 0:
            print("\n".join([str(x) for x in lista_menores]))
        else:
            print(f"No hay elementos menores a {numero}")

    def eliminar(self, numero):
        ''' Elimina el numero de la lista '''
        if numero not in self.lista_numeros:
            print(f"El numero: {numero} no se encuentra en la lista, no se puede eliminar")
        else:
            self.lista_numeros.remove(numero)
            print(f"{numero} eliminado")

    def conteo(self):
        ''' Calcula tupla con elemento y numero de ocurrencias '''
        set_numeros = set(self.lista_numeros)
        tupla_conteo = [(x, self.lista_numeros.count(x)) for x in set_numeros]
        print("\n".join([str(x) for x in tupla_conteo]))


def main():
    solicitar = True
    lista_numeros = []
    
    print("Creando una lista, empecemos ingresando números:")
    while solicitar:
        numero_str = input("Ingrese numero:\t")
        numero = Numeros.valida_numero(numero_string=numero_str)
        if numero is not None and numero != 0:
            lista_numeros.append(numero)
        if numero == 0:
            solicitar = False
    numero_objeto = Numeros(lista_numeros=lista_numeros)
    print('\n')
    print(f"Listo, números ingresados, la lista es la siguiente:")
    print(numero_objeto)

    time.sleep(2)
    print('\n')
    solicitar_eliminar = True
    while solicitar_eliminar:
        numero_str = input("Ingrese número a eliminar:\t")
        numero = Numeros.valida_numero(numero_string=numero_str)
        if numero is None:
            continue
        numero_objeto.eliminar(numero=numero)
        solicitar_eliminar = False
    print('\n')
    print(f"Listo, la lista es la siguiente:")
    print(numero_objeto)

    time.sleep(2)
    print('\n')
    print("Suma de los elementos de la lista ingresada")
    numero_objeto.suma()

    time.sleep(2)
    print('\n')
    print("Ingrese un número y te mostraré los elementos, de la lista, menores a ese número")
    solicitar_menores = True
    while solicitar_menores:
        numero_str = input("Ingrese número:\t")
        numero = Numeros.valida_numero(numero_string=numero_str)
        if numero is None:
            continue
        numero_objeto.get_menores(numero=numero)
        solicitar_menores = False

    time.sleep(2)
    print('\n')
    print("A continuación muestro un conteo por cada elemento de la lista")
    numero_objeto.conteo()

    print('\n')
    input("Presione cualquier tecla para salir de la aplicación")


if __name__ == '__main__':
    main()