# Calcular planilla de 3 empleados A, B, Y C, cada uno con diferente tarifa

import tkinter as tk
from tkinter import messagebox

# Datos de empleados
empleados = {
    'A': 2.10,
    'B': 3.10,
    'C': 3.80
}

def calcular_sueldos():
    try:
        horas_a = float(entry_a.get())
        horas_b = float(entry_b.get())
        horas_c = float(entry_c.get())
        
        # Obtener pagos extra (si están vacíos, usar 0)
        pago_extra_a = float(entry_extra_a.get()) if entry_extra_a.get() else 0
        pago_extra_b = float(entry_extra_b.get()) if entry_extra_b.get() else 0
        pago_extra_c = float(entry_extra_c.get()) if entry_extra_c.get() else 0
        
        # Calcular sueldos base + pagos extra
        sueldo_a = (horas_a * empleados['A']) + pago_extra_a
        sueldo_b = (horas_b * empleados['B']) + pago_extra_b
        sueldo_c = (horas_c * empleados['C']) + pago_extra_c
        
        # Calcular total
        total_salarios = sueldo_a + sueldo_b + sueldo_c
        
        resultado.set(
            f"Sueldo A: ${sueldo_a:.2f}\n"
            f"Sueldo B: ${sueldo_b:.2f}\n"
            f"Sueldo C: ${sueldo_c:.2f}\n"
            f"{'='*25}\n"
            f"TOTAL SALARIOS: ${total_salarios:.2f}"
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa solo números válidos.")

def limpiar_pantalla():
    # Limpiar todas las entradas
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_extra_a.delete(0, tk.END)
    entry_extra_b.delete(0, tk.END)
    entry_extra_c.delete(0, tk.END)
    
    # Limpiar resultado
    resultado.set("")

# Crear ventana
ventana = tk.Tk()
ventana.title("Cálculo de Planilla")
ventana.geometry("400x500")

# Etiquetas y entradas para horas trabajadas
tk.Label(ventana, text="HORAS TRABAJADAS", font=('Arial', 12, 'bold')).grid(row=0, columnspan=2, pady=(10,5))

tk.Label(ventana, text="Horas trabajadas por A:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_a = tk.Entry(ventana)
entry_a.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Horas trabajadas por B:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_b = tk.Entry(ventana)
entry_b.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Horas trabajadas por C:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_c = tk.Entry(ventana)
entry_c.grid(row=3, column=1, padx=10, pady=5)

# Separador y etiquetas para pagos extra
tk.Label(ventana, text="PAGOS EXTRA", font=('Arial', 12, 'bold')).grid(row=4, columnspan=2, pady=(20,5))

tk.Label(ventana, text="Pago extra para A:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
entry_extra_a = tk.Entry(ventana)
entry_extra_a.grid(row=5, column=1, padx=10, pady=5)

tk.Label(ventana, text="Pago extra para B:").grid(row=6, column=0, padx=10, pady=5, sticky='e')
entry_extra_b = tk.Entry(ventana)
entry_extra_b.grid(row=6, column=1, padx=10, pady=5)

tk.Label(ventana, text="Pago extra para C:").grid(row=7, column=0, padx=10, pady=5, sticky='e')
entry_extra_c = tk.Entry(ventana)
entry_extra_c.grid(row=7, column=1, padx=10, pady=5)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=8, columnspan=2, pady=20)

tk.Button(frame_botones, text="Calcular Sueldos", command=calcular_sueldos, 
         bg='lightgreen', font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=5)

tk.Button(frame_botones, text="Limpiar Pantalla", command=limpiar_pantalla, 
         bg='lightcoral', font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=5)

# Área de resultados
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, justify="left", font=('Arial', 12), 
         bg='lightyellow', relief='sunken', padx=10, pady=10).grid(row=9, columnspan=2, pady=20, padx=20, sticky='ew')

# Configurar el peso de las columnas para que se expandan
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

# Ejecutar la ventana
ventana.mainloop()
