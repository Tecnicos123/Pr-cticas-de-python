import tkinter as tk
from tkinter import messagebox

def calcular_salarios():
    try:
        dias1 = float(entry_dias_emp1.get())
        dias2 = float(entry_dias_emp2.get())
        
        horas = 8
        tarifa1 = 2.77
        tarifa2 = 2.91

        salario_emp1 = dias1 * horas * tarifa1
        salario_emp2 = dias2 * horas * tarifa2
        total_salarios = salario_emp1 + salario_emp2

        riesgos_prof = total_salarios * 0.0098
        seguro_edu = total_salarios * 0.0275
        seguro_social = total_salarios * 0.36656
        cuota_css = riesgos_prof + seguro_edu + seguro_social

        resultado.set(
            f"Empleado 1 (N): B/ {salario_emp1:.2f}\n"
            f"Empleado 2 (S): B/ {salario_emp2:.2f}\n"
            f"Total salario: B/ {total_salarios:.2f}\n"
            f"Cuota mensual CSS: B/ {cuota_css:.2f}"
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Cálculo de Salario Mensual")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Días laborados - Empleado 1 (N):").grid(row=0, column=0, sticky="e")
entry_dias_emp1 = tk.Entry(ventana)
entry_dias_emp1.grid(row=0, column=1)

tk.Label(ventana, text="Días laborados - Empleado 2 (S):").grid(row=1, column=0, sticky="e")
entry_dias_emp2 = tk.Entry(ventana)
entry_dias_emp2.grid(row=1, column=1)

# Botón para calcular
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular_salarios)
btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Área de resultado
resultado = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado, justify="left")
label_resultado.grid(row=3, column=0, columnspan=2)

# Ejecutar ventana
ventana.mainloop()
