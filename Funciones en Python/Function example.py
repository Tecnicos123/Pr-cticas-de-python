'''
Ejemplo de una función básica:

Una función, es un modo de programar donde se pueden definir variables, expresiones y sentencias de control con el fin de realizar una o n veces, determinadas acciones, teniendo en cuenta, que solo se van a ejecutar cuando son llamadas.
'''
a = 10
b = 5

# sum function
def suma(x, y):
    return x + y
# Llamada a la función
resultado = suma(a, b)
print(f'La suma de {a} y {b} es: {resultado}')

# Enter two integers to add them
def suma2():
    x = int(input("Ingrese el primer valor: "))
    y = int(input("Ingrese el segundo valor: "))
    return x + y
# Llamada a la función
resultado2 = suma2()
print(f'La suma de los valores ingresados es: {resultado2}')

# Y si queremos que sume números decimales?
def suma3():
    x = float(input("Ingrese el primer valor: "))
    y = float(input("Ingrese el segundo valor: "))
    return x + y
# Llamada a la función
resultado3 = suma3()
print(f'La suma de los valores ingresados es: {resultado3}')


# Y si queremos que sume números decimales y enteros?
def suma4():
    x = float(input("Ingrese el primer valor: "))
    y = int(input("Ingrese el segundo valor: "))
    return x + y
# Llamada a la función
resultado4 = suma4()
print(f'La suma de los valores ingresados es: {resultado4}')


# Y si queremos que sume números decimales y enteros, pero el resultado sea un número entero?
def suma5():
    x = float(input("Ingrese el primer valor: "))
    y = int(input("Ingrese el segundo valor: "))
    return int(x + y)
# Llamada a la función
resultado5 = suma5()
print(f'La suma de los valores ingresados es: {resultado5}')


# Y si queremos que sume números decimales y enteros, pero el resultado sea un número decimal?
def suma6():
    x = float(input("Ingrese el primer valor: "))
    y = int(input("Ingrese el segundo valor: "))
    return x + y
# Llamada a la función
resultado6 = suma6()
print(f'La suma de los valores ingresados es: {resultado6}')
