'''
Fuente: https://platzi.com/tutoriales/4227-python-fundamentos/25624-mi-primer-proyecto-python/

Calcular el promedio de notas de tres alumnos basado en las siguientes condiciones:
a) Cada alumno posee tres notas diferentes
b) Debemos calcular el promedio de los tres alumnos
c) Determinar cual es el mejor promedio

Los datos de los alumnos son los siguientes

Nombre Nota 1 Nota 2 Nota 3
Pedro Lopez 10 8 7
Juan Martinez 6 10 10
María Cruz 10 10 9
'''

alumnos = [
    ['Pedro López' , 10, 8, 7],
    ['Juan Martínez' , 6, 10, 10],
    ['María Cruz' , 10, 10 , 9]
]

# Inicializamos el mayor de los promedios
mayorPromedio = 0.0
nombreMejor = ""
# Ciclo de calculos de los promedios de cada alumno
for alumno in alumnos:
    promedioAlumno = (alumno[1] + alumno[2] + alumno[3]) / 3
    nombreAlumno = alumno[0]
    print(f"El promedio de {nombreAlumno} es: {promedioAlumno:.2f}")
    if (promedioAlumno > mayorPromedio):
        mayorPromedio = promedioAlumno
        nombreMejor = nombreAlumno
print("--------------------")
print(f"El mejor promedio es de {nombreMejor} con un promedio de {mayorPromedio:.2f}")
print("Fin del programa")

'''
Algunas mejoras que podríamos introducir sería por ejempplo que el usuario digite el nombre del alumno así como sus tres notas y de esa manera crear de forma dinámica la lista lo cual podríamos incluso no limitar a 3 alumnos, sino mas si así lo deseáramos introduciendo una modificación, con el cliclo While.

En este caso tendríamos que establecer una condición de control que permita establecer cuando el usuario dejará de introducir datos; con cada iteración de introduce el nombre del alumno, las tres notas y luego se pregunta si desea seguir procesando mas alumnos, si el usuario determina que no, se proceden a los cálculos, de lo contrario se seguirá almacenando información.

Se inicializaran dos listas que almacenarán los datos de un alumno inclucyendo las notas y una segunda lista que será la lista de todos los alumnos incluidos

El código de llenado sería como este:
'''
# Inicializar las listas y variables
alumno = []
alumnos = []
respuesta = True
mayorPromedio = 0  # Inicializar el mayor promedio

while respuesta:
    nombre = input("Suministre el nombre del alumno: ")
    n1 = float(input("Ingrese la nota 1: "))  # Acepta decimales
    n2 = float(input("Ingrese la nota 2: "))  # Acepta decimales
    n3 = float(input("Ingrese la nota 3: "))  # Acepta decimales
    
    # Crear una nueva lista para cada alumno
    alumno = [nombre, n1, n2, n3]
    
    # Almacenar este alumno en la lista de alumnos
    alumnos.append(alumno)
    
    seguir = input("Introduzca S para continuar, de lo contrario se pasará a los cálculos. ¿Desea continuar? S/N: ")
    seguir = seguir.lower()
    if seguir != "s":
        respuesta = False

# Ahora se procede a los cálculos
print("\n--- RESULTADOS ---")
nombreMejor = ""

for alumno in alumnos:
    promedioAlumno = (alumno[1] + alumno[2] + alumno[3]) / 3
    nombreAlumno = alumno[0]
    print(f"El promedio de {nombreAlumno} es: {promedioAlumno:.2f}")
    
    if promedioAlumno > mayorPromedio:
        mayorPromedio = promedioAlumno
        nombreMejor = nombreAlumno

print("--------------------")
print(f"El mejor promedio es de {nombreMejor} con un promedio de {mayorPromedio:.2f}")
print("Fin del programa")

'''
El siguiente código es una versión mejorada del anterior, en el cual se permite ingresar más notas para cada alumno, no limitándose a solo tres notas. Además, se pregunta al usuario si desea ingresar más notas para cada alumno.

También se puede modificar para que me pregunte si deseo ingresar más notas
'''

# Inicializar las listas y variables
alumno = []
alumnos = []
respuesta = True
mayorPromedio = 0  # Inicializar el mayor promedio

while respuesta:
    nombre = input("Suministre el nombre del alumno: ")
    
    # Lista para almacenar todas las notas del alumno
    notas = []
    
    # Ingresar las tres primeras notas
    for i in range(1, 4):
        nota = float(input(f"Ingrese la nota {i}: "))
        notas.append(nota)
    
    # Preguntar si se desean ingresar más notas
    while True:
        agregar = input("¿Desea ingresar otra nota para este alumno? S/N: ").lower()
        if agregar == "s":
            nota_extra = float(input("Ingrese la nota adicional: "))
            notas.append(nota_extra)
        else:
            break
    
    # Crear la lista del alumno: nombre seguido de todas las notas
    alumno = [nombre] + notas
    
    # Almacenar este alumno en la lista de alumnos
    alumnos.append(alumno)
    
    seguir = input("¿Desea ingresar otro alumno? S/N: ").lower()
    if seguir != "s":
        respuesta = False

# Ahora se procede a los cálculos
print("\n--- RESULTADOS ---")
nombreMejor = ""

for alumno in alumnos:
    nombreAlumno = alumno[0]
    notasAlumno = alumno[1:]  # todas las notas del alumno
    promedioAlumno = sum(notasAlumno) / len(notasAlumno)
    print(f"El promedio de {nombreAlumno} es: {promedioAlumno:.2f}")
    
    if promedioAlumno > mayorPromedio:
        mayorPromedio = promedioAlumno
        nombreMejor = nombreAlumno

print("--------------------")
print(f"El mejor promedio es de {nombreMejor} con un promedio de {mayorPromedio:.2f}")
print("Fin del programa")
