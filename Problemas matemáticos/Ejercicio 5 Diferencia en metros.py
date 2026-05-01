"""
Dos escaladores quieren subir a una torre, el primero sube a una torre de 4300 mts,
y el segundo sube a una torre de 45 km.
¿Cuál es la diferencia en metros entre un escalador y otro?
"""

# Datos del problema
altura1 = 4300      # metros
altura2_km = 45     # kilómetros

# Conversión a metros
altura2 = altura2_km * 1000

# Cálculo de la diferencia
diferencia = altura2 - altura1

print("=== DIFERENCIA DE ALTURA ===")
print(f"Primer escalador:  {altura1} metros")
print(f"Segundo escalador: {altura2} metros")
print(f"Diferencia:        {diferencia} metros")