"""
Una tubería tiene un flujo de agua de 3 lts por segundo,
¿Cuántos litros de agua pasan por la tubería en 1 minuto? R=180 litros por minutos
"""

flujo = float(input("Ingrese el flujo en litros por segundo: "))
tiempo_segundos = 60
resultado = flujo * tiempo_segundos
print(f"En 1 minuto pasan {resultado} litros de agua")