import tkinter as tk
from tkinter import messagebox

def calcular_porcentajes():
    try:
        # Obtener los valores de los campos de entrada
        votos_favor = int(entry_favor.get())
        votos_contra = int(entry_contra.get())
        
        # Validar que los números sean positivos
        if votos_favor < 0 or votos_contra < 0:
            messagebox.showerror("Error", "Los números deben ser positivos")
            return
        
        total = votos_favor + votos_contra
        
        if total > 0:
            porcentaje_favor = votos_favor / total * 100
            porcentaje_contra = votos_contra / total * 100
            
            # Mostrar los resultados
            resultado_favor.config(text=f"A favor: {porcentaje_favor:.2f}%")
            resultado_contra.config(text=f"En contra: {porcentaje_contra:.2f}%")
            resultado_total.config(text=f"Total de votos: {total}")
        else:
            messagebox.showwarning("Advertencia", "No hay votos registrados")
            
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos")

def limpiar_campos():
    entry_favor.delete(0, tk.END)
    entry_contra.delete(0, tk.END)
    resultado_favor.config(text="A favor: --%")
    resultado_contra.config(text="En contra: --%")
    resultado_total.config(text="Total de votos: --")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Porcentajes - Votos Parlamentarios")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Título
titulo = tk.Label(ventana, text="Porcentaje de los parlamentarios", 
                 font=("Arial", 16, "bold"), fg="darkblue")
titulo.pack(pady=10)

# Frame para los campos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Campo para votos a favor
tk.Label(frame_entrada, text="Votos a favor:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_favor = tk.Entry(frame_entrada, font=("Arial", 10), width=15)
entry_favor.grid(row=0, column=1, padx=5, pady=5)

# Campo para votos en contra
tk.Label(frame_entrada, text="Votos en contra:", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_contra = tk.Entry(frame_entrada, font=("Arial", 10), width=15)
entry_contra.grid(row=1, column=1, padx=5, pady=5)

# Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

# Botones
btn_calcular = tk.Button(frame_botones, text="Calcular", command=calcular_porcentajes,
                        bg="green", fg="white", font=("Arial", 10, "bold"), width=12)
btn_calcular.pack(side=tk.LEFT, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_campos,
                       bg="orange", fg="white", font=("Arial", 10, "bold"), width=12)
btn_limpiar.pack(side=tk.LEFT, padx=5)

# Frame para los resultados
frame_resultados = tk.Frame(ventana)
frame_resultados.pack(pady=10)

# Etiquetas para mostrar los resultados
resultado_favor = tk.Label(frame_resultados, text="A favor: --%", 
                          font=("Arial", 12, "bold"), fg="darkgreen")
resultado_favor.pack(pady=2)

resultado_contra = tk.Label(frame_resultados, text="En contra: --%", 
                           font=("Arial", 12, "bold"), fg="darkred")
resultado_contra.pack(pady=2)

resultado_total = tk.Label(frame_resultados, text="Total de votos: --", 
                          font=("Arial", 10), fg="darkblue")
resultado_total.pack(pady=2)

# Permitir calcular con Enter
def calcular_con_enter(event):
    calcular_porcentajes()

ventana.bind('<Return>', calcular_con_enter)

# Ejecutar la aplicación
ventana.mainloop()
