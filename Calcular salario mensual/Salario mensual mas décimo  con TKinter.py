#Calculo de horas laboradas en el mes por la tarifa por hora
#EL propósito es obtener el salrio mensual
#Empleado 1 N B/2.77
#empleado 2 S B/2.91

import tkinter as tk
from tkinter import messagebox

def calcular_salario(dias_laborados, costo_hora, horas_diarias=8):
    return dias_laborados * horas_diarias * costo_hora

def calcular_cuotas_css(salario_total, decimo):
    base_calculo = salario_total + decimo
    riesgos_prof = base_calculo * 0.0098
    seguro_edu = base_calculo * 0.02159
    seguro_social = base_calculo * 0.34056
    total = riesgos_prof + seguro_edu + seguro_social

    return {
        'riesgos_prof': riesgos_prof,
        'seguro_edu': seguro_edu,
        'seguro_social': seguro_social,
        'total': total
    }

def calcular():
    try:
        dias_emp1 = float(entry_dias_emp1.get())
        dias_emp2 = float(entry_dias_emp2.get())
        decimo = float(entry_decimo.get())

        salario_emp1 = calcular_salario(dias_emp1, 2.77)
        salario_emp2 = calcular_salario(dias_emp2, 2.91)

        total_salarios = salario_emp1 + salario_emp2

        cuotas = calcular_cuotas_css(total_salarios, decimo)

        resultado = f"""
===== RESUMEN =====
Salario Empleado N: B/ {salario_emp1:.2f}
Salario Empleado S: B/ {salario_emp2:.2f}
Total de salarios: B/ {total_salarios:.2f}
Décimo: B/ {decimo:.2f}

===== CUOTAS CSS =====
Riesgos Profesionales: B/ {cuotas['riesgos_prof']:.2f}
Seguro Educativo: B/ {cuotas['seguro_edu']:.2f}
Seguro Social: B/ {cuotas['seguro_social']:.2f}
Total Cuotas CSS: B/ {cuotas['total']:.2f}
"""
        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, resultado)

    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor ingrese valores numéricos válidos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Salario y CSS")
ventana.geometry("500x500")

# Entradas
tk.Label(ventana, text="Días laborados Empleado N (B/2.77 por hora):").pack()
entry_dias_emp1 = tk.Entry(ventana)
entry_dias_emp1.pack()

tk.Label(ventana, text="Días laborados Empleado S (B/2.91 por hora):").pack()
entry_dias_emp2 = tk.Entry(ventana)
entry_dias_emp2.pack()

tk.Label(ventana, text="Décimo total:").pack()
entry_decimo = tk.Entry(ventana)
entry_decimo.pack()

# Botón de cálculo
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

# Resultado
text_resultado = tk.Text(ventana, height=15, width=60)
text_resultado.pack()

ventana.mainloop()
