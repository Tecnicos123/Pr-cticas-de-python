class Estudiante:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = []
    
    def agregar_nota(self, nota):
        """Agrega una nota individual"""
        self.notas.append(nota)
    
    def agregar_notas(self, lista_notas):
        """Agrega múltiples notas de una vez"""
        self.notas.extend(lista_notas)
    
    def calcular_promedio(self):
        """Calcula el promedio de todas las notas"""
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def mostrar_informacion(self):
        """Muestra toda la información del estudiante"""
        promedio = self.calcular_promedio()
        print(f"Estudiante: {self.nombre} {self.apellido}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {promedio:.2f}")
        print("-" * 30)

# Crear los estudiantes
juan = Estudiante("Juan", "Gonzalez.")
pedro = Estudiante("Pedro", "Aguilar.")
dagoberto = Estudiante("Dagoberto", "Lara")

# Agregar las notas
juan.agregar_notas([3.5, 4.5, 4.9, 5.0])
pedro.agregar_notas([3.3, 3.6, 4.5, 4.8])
dagoberto.agregar_notas([4.5, 4.8, 4.9, 3.5])

# Mostrar información de cada estudiante
juan.mostrar_informacion()
pedro.mostrar_informacion()
dagoberto.mostrar_informacion()

# También puedes agregar notas una por una si quieres
# juan.agregar_nota(4.2)
# print(f"Nuevo promedio de Juan: {juan.calcular_promedio():.2f}")

# Crear una lista de estudiantes para manejar múltiples estudiantes
estudiantes = [juan, pedro, dagoberto]

print("REPORTE GENERAL:")
print("=" * 40)
for estudiante in estudiantes:
    print(f"{estudiante.nombre} {estudiante.apellido}: {estudiante.calcular_promedio():.2f}")

# Funciones para análisis de la clase
def encontrar_mejor_estudiante(lista_estudiantes):
    """Encuentra y retorna el estudiante con el mejor promedio"""
    if not lista_estudiantes:
        return None
    
    mejor_estudiante = lista_estudiantes[0]
    mejor_promedio = mejor_estudiante.calcular_promedio()
    
    for estudiante in lista_estudiantes:
        promedio_actual = estudiante.calcular_promedio()
        if promedio_actual > mejor_promedio:
            mejor_promedio = promedio_actual
            mejor_estudiante = estudiante
    
    return mejor_estudiante

def encontrar_peor_estudiante(lista_estudiantes):
    """Encuentra y retorna el estudiante con el promedio más bajo"""
    if not lista_estudiantes:
        return None
    
    peor_estudiante = lista_estudiantes[0]
    peor_promedio = peor_estudiante.calcular_promedio()
    
    for estudiante in lista_estudiantes:
        promedio_actual = estudiante.calcular_promedio()
        if promedio_actual < peor_promedio:
            peor_promedio = promedio_actual
            peor_estudiante = estudiante
    
    return peor_estudiante

def calcular_promedio_clase(lista_estudiantes):
    """Calcula el promedio general de toda la clase"""
    if not lista_estudiantes:
        return 0
    
    suma_promedios = sum(estudiante.calcular_promedio() for estudiante in lista_estudiantes)
    return suma_promedios / len(lista_estudiantes)

def contar_aprobados_reprobados(lista_estudiantes, nota_minima=3.0):
    """Cuenta cuántos estudiantes aprobaron y reprobaron"""
    aprobados = 0
    reprobados = 0
    
    for estudiante in lista_estudiantes:
        if estudiante.calcular_promedio() >= nota_minima:
            aprobados += 1
        else:
            reprobados += 1
    
    return aprobados, reprobados

# ANÁLISIS COMPLETO DE LA CLASE
print("\n" + "=" * 50)
print("📊 ANÁLISIS COMPLETO DE LA CLASE")
print("=" * 50)

# Mejor estudiante
print("🏆 MEJOR ESTUDIANTE:")
mejor = encontrar_mejor_estudiante(estudiantes)
if mejor:
    print(f"   Nombre: {mejor.nombre} {mejor.apellido}")
    print(f"   Promedio: {mejor.calcular_promedio():.2f}")
    print(f"   Notas: {mejor.notas}")

print()

# Peor estudiante
print("📉 ESTUDIANTE CON PROMEDIO MÁS BAJO:")
peor = encontrar_peor_estudiante(estudiantes)
if peor:
    print(f"   Nombre: {peor.nombre} {peor.apellido}")
    print(f"   Promedio: {peor.calcular_promedio():.2f}")
    print(f"   Notas: {peor.notas}")

print()

# Promedio general de la clase
promedio_clase = calcular_promedio_clase(estudiantes)
print(f"📈 PROMEDIO GENERAL DE LA CLASE: {promedio_clase:.2f}")

print()

# Estadísticas de aprobados/reprobados
aprobados, reprobados = contar_aprobados_reprobados(estudiantes, 3.0)
total_estudiantes = len(estudiantes)
porcentaje_aprobados = (aprobados / total_estudiantes) * 100 if total_estudiantes > 0 else 0

print("✅ ESTADÍSTICAS DE APROBACIÓN (Nota mínima: 3.0):")
print(f"   Total de estudiantes: {total_estudiantes}")
print(f"   Aprobados: {aprobados} ({porcentaje_aprobados:.1f}%)")
print(f"   Reprobados: {reprobados} ({100-porcentaje_aprobados:.1f}%)")

print("\n" + "=" * 50)