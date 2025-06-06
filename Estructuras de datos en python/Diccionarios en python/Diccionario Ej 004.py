'''
Diccionario
Un diccionario en Python es una colección de pares clave-valor. Cada clave está conectada a un valor y puede usar una clave para acceder al valor asociado con esa clave.
El valor de una clave puede ser un número, una cadena, una lista o incluso otro diccionario.
De hecho, puede utilizar cualquier objeto que pueda crear en Python como valor en un diccionario.

Ejercicio
Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo: “r”:5, “%”:3, “a”:8, “9”:1.
'''
from typing import List


class String:
    def __init__(self, lista_string: List):
        self.lista_string = lista_string
        self.diccionario_cantidad = {}

        self.de_lista_a_diccionario()

    def de_lista_a_diccionario(self) -> None:
        ''' convierte la lista de string a un diccionario con la cantidad de cada string '''
        for string in self.lista_string:
            if string not in self.diccionario_cantidad:
                self.diccionario_cantidad[string] = 0
            self.diccionario_cantidad[string] += 1

    def __str__(self) -> str:
        ''' Muestra la cantidad de ocurrencias de cada string '''
        text = 'Conteo de elementos:'
        for clave, valor in self.diccionario_cantidad.items():
            text += f'\n{clave}: {valor}'
        return text


def main():
    cantidad_string = 0
    lista_string = []

    while cantidad_string < 50:
        cantidad_string += 1
        string = input(f"Ingrese string {cantidad_string}:\t")
        lista_string.append(string)

    string_ = String(lista_string=lista_string)
    print(string_)

    print('\n')
    input("Presione cualquier tecla para salir de la aplicación")


if __name__ == '__main__':
    main()