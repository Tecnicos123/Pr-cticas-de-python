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
