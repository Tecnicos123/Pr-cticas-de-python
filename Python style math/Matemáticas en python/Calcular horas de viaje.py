# Un vehículo parte de la ciudad de Cóedoba y se dirige a Rosario por autopista.
# La distancia aproximada entre ambas ciudades es de 400 kilómetros.
# El vehículo se desplaza con velocidad promedio de 122 km/h.

# Desarrolle un programa que calcule el tiempo total en horas que demorará ese vehículo en llegar a Rosario.

velocidad_promedio = 122

print("Calculo de tiempo de llegada en un viaje: ")

horas = 400 / velocidad_promedio
horas_redondeadas = round(horas)  # Redondea al entero más cercano

print("La cantidad de horas que tarda de Córdoba a Rosario es de ", horas)

print("La cantidad de horas que tarda de Córdoba a Rosario es de ", horas_redondeadas)

# Otra manera de resolver este problema es usando una función en python
print("\nUsando una función para calcular el tiempo de viaje:")

def calcular_tiempo(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo

# Datos del problema
distancia = 400  # km
velocidad = 122  # km/h

# Calcular el tiempo
tiempo_total = calcular_tiempo(distancia, velocidad)

print(f"El tiempo total de viaje es de {tiempo_total:.0f} horas.")

# Tambien lo podemos modificar para que retorne el tiempo en horas y minutos
def calcular_tiempo_horas_minutos(distancia, velocidad):
    tiempo = distancia / velocidad
    horas = int(tiempo)
    minutos = int((tiempo - horas) * 60)
    return horas, minutos

# Calcular el tiempo en horas y minutos
horas_totales, minutos_totales = calcular_tiempo_horas_minutos(distancia, velocidad)
print(f"El tiempo total de viaje es de {horas_totales} horas y {minutos_totales} minutos.")

# Y si deseamos que el programa me pida los datos de entrada, como el kilometraje y la distancia, podemos hacer lo siguiente:

def calcular_tiempo(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo

# Pedir los datos al usuario
distancia = float(input("Ingresa la distancia entre las ciudades en kilómetros: "))
velocidad = float(input("Ingresa la velocidad promedio del vehículo en km/h: "))

# Calcular el tiempo
tiempo_total = calcular_tiempo(distancia, velocidad)

print(f"El tiempo total de viaje es de {tiempo_total:.0f} horas.")
