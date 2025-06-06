'''
Conjuntos
La principal característica de este tipo de estructura de datos es que es una colección cuyos elementos son únicos y no guardan ningún orden.

Los principales uso de los conjuntos son conocer si un elemento pertenece o no a una colección y eliminar duplicados de una lista, tupla, string, …

Este tipo de estructuras implementa las típicas operaciones matemáticas sobre conjuntos: intersección, unión, diferencia, …

Ejercicio
Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.

Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
'''
import time
from typing import List


class Nombres(object):

    @staticmethod
    def ingresar_nombres():
        ''' Método para crear lista con nombres ingresados '''
        lista_nombres = []
        solicitar = True
        while solicitar:
            nombre = input("Ingrese nombre:\t")
            if len(nombre) == 0:
                print("Nombre no válido, ingrese otro nombre")
                continue
            if nombre != '?x?':
                lista_nombres.append(nombre)
            else:
                solicitar = False
        return lista_nombres

    def __init__(self, nombres_primaria: List, nombres_secundaria: List):
        self.nombres_primaria = set(nombres_primaria)
        self.nombres_secundaria = set(nombres_secundaria)

    @staticmethod
    def mostrar_set(set_elementos):
        ''' Método para mostrar una lista de nombres '''
        if len(set_elementos) > 0:
            print("\n".join([str(x) for x in set_elementos]))
        else:
            print("No hay elementos")

    def get_nombres(self):
        ''' Mostrar todos los nombres de la lista '''
        todos_nombres = self.nombres_primaria.union(self.nombres_secundaria)
        return self.mostrar_set(todos_nombres)

    def comun(self):
        ''' Mostrar nombres en comun en ambos conjuntos '''
        nombres_comun = self.nombres_primaria.intersection(self.nombres_secundaria)
        return self.mostrar_set(nombres_comun)

    def diferentes(self):
        ''' Mostrar nombres diferentes: nombre primaria - nombre secundaria '''
        diferentes = self.nombres_primaria - self.nombres_secundaria
        return self.mostrar_set(diferentes)


def main():
    print("Aplicación de nombres")
    print("Empecemos ingresando nombres de primaria")
    nombres_primaria = Nombres.ingresar_nombres()

    print('\n')
    print("Ahora vamos con nombres de secundaria")
    nombres_secundaria = Nombres.ingresar_nombres()

    nombres = Nombres(nombres_primaria=nombres_primaria, nombres_secundaria=nombres_secundaria)
    print('\n')
    print(f"Listo, nombres ingresados")

    time.sleep(2)
    print('\n')
    print("Todos los nombres:")
    nombres.get_nombres()

    time.sleep(2)
    print('\n')
    print("Nombres en común:")
    nombres.comun()

    time.sleep(2)
    print('\n')
    print("Nombres de primaria que no están en secundaria:")
    nombres.diferentes()

    print('\n')
    input("Presione cualquier tecla para salir de la aplicación")


if __name__ == '__main__':
    main()