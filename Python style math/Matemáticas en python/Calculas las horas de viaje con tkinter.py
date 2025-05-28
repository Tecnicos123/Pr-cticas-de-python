# Programa para calculas las horas de viaje, solicitando los datos de entrada y con interfaz gráfica tkinter

import tkinter as tk
from tkinter import messagebox

def calcular_tiempo(distancia, velocidad):
    # Calcular el tiempo en horas
    tiempo_horas = distancia / velocidad
    # Convertir las horas en horas y minutos
    horas = int(tiempo_horas)
    minutos = round((tiempo_horas - horas) * 60)
    return horas, minutos

def calcular():
    try:
        # Obtener los valores de los campos de texto
        distancia = float(entry_distancia.get())
        velocidad = float(entry_velocidad.get())

        # Verificar que los valores sean positivos
        if distancia <= 0 or velocidad <= 0:
            raise ValueError("Los valores deben ser mayores que cero.")
        
        # Calcular el tiempo
        horas, minutos = calcular_tiempo(distancia, velocidad)
        
        # Mostrar el resultado en el label
        label_resultado.config(text=f"Tiempo total de viaje: {horas} horas y {minutos} minutos.")
    
    except ValueError as e:
        # En caso de que los valores no sean válidos
        messagebox.showerror("Error", f"Entrada incorrecta: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de tiempo de viaje")

# Crear los widgets
label_distancia = tk.Label(ventana, text="Distancia (km):")
label_distancia.pack()

entry_distancia = tk.Entry(ventana)
entry_distancia.pack()

label_velocidad = tk.Label(ventana, text="Velocidad (km/h):")
label_velocidad.pack()

entry_velocidad = tk.Entry(ventana)
entry_velocidad.pack()

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()

label_resultado = tk.Label(ventana, text="Tiempo total de viaje: ")
label_resultado.pack()

# Iniciar el bucle de la interfaz
ventana.mainloop()