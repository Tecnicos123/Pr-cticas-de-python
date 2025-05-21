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