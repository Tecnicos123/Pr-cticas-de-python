import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

class GeneradorPiramides:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Pirámides Numéricas")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Variables
        self.altura_var = tk.StringVar(value="5")
        self.estilo_var = tk.StringVar(value="espaciado")
        self.fuente_var = tk.StringVar(value="Courier")
        self.tamaño_fuente_var = tk.StringVar(value="12")
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Título principal
        titulo = tk.Label(
            self.root, 
            text="🔢 Generador de Pirámides Numéricas 🔢",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        titulo.pack(pady=20)
        
        # Frame de controles
        frame_controles = tk.Frame(self.root, bg="#f0f0f0")
        frame_controles.pack(pady=10, padx=20, fill="x")
        
        # Configuración de altura
        frame_altura = tk.Frame(frame_controles, bg="#f0f0f0")
        frame_altura.pack(side="left", padx=10)
        
        tk.Label(frame_altura, text="Altura:", font=("Arial", 12), bg="#f0f0f0").pack()
        altura_spinbox = tk.Spinbox(
            frame_altura,
            from_=1, to=15,
            textvariable=self.altura_var,
            width=5,
            font=("Arial", 12)
        )
        altura_spinbox.pack(pady=5)
        
        # Estilo de pirámide
        frame_estilo = tk.Frame(frame_controles, bg="#f0f0f0")
        frame_estilo.pack(side="left", padx=20)
        
        tk.Label(frame_estilo, text="Estilo:", font=("Arial", 12), bg="#f0f0f0").pack()
        estilo_combo = ttk.Combobox(
            frame_estilo,
            textvariable=self.estilo_var,
            values=["espaciado", "compacto"],
            width=10,
            state="readonly"
        )
        estilo_combo.pack(pady=5)
        
        # Configuración de fuente
        frame_fuente = tk.Frame(frame_controles, bg="#f0f0f0")
        frame_fuente.pack(side="left", padx=20)
        
        tk.Label(frame_fuente, text="Fuente:", font=("Arial", 12), bg="#f0f0f0").pack()
        fuente_combo = ttk.Combobox(
            frame_fuente,
            textvariable=self.fuente_var,
            values=["Courier", "Arial", "Times", "Consolas"],
            width=10,
            state="readonly"
        )
        fuente_combo.pack(pady=2)
        
        tamaño_spinbox = tk.Spinbox(
            frame_fuente,
            from_=8, to=20,
            textvariable=self.tamaño_fuente_var,
            width=5
        )
        tamaño_spinbox.pack(pady=3)
        
        # Botones
        frame_botones = tk.Frame(self.root, bg="#f0f0f0")
        frame_botones.pack(pady=20)
        
        btn_generar = tk.Button(
            frame_botones,
            text="🎲 Generar Pirámide",
            command=self.generar_piramide,
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        btn_generar.pack(side="left", padx=10)
        
        btn_limpiar = tk.Button(
            frame_botones,
            text="🗑️ Limpiar",
            command=self.limpiar_texto,
            font=("Arial", 12),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        btn_limpiar.pack(side="left", padx=10)
        
        btn_multiple = tk.Button(
            frame_botones,
            text="🔄 Múltiples (5)",
            command=self.generar_multiples,
            font=("Arial", 12),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        btn_multiple.pack(side="left", padx=10)
        
        btn_exportar = tk.Button(
            frame_botones,
            text="💾 Copiar",
            command=self.copiar_texto,
            font=("Arial", 12),
            bg="#f39c12",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        btn_exportar.pack(side="left", padx=10)
        
        # Área de texto para mostrar pirámides
        frame_texto = tk.Frame(self.root, bg="#f0f0f0")
        frame_texto.pack(pady=20, padx=20, fill="both", expand=True)
        
        tk.Label(
            frame_texto, 
            text="Pirámides Generadas:",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        ).pack(anchor="w")
        
        self.texto_area = scrolledtext.ScrolledText(
            frame_texto,
            width=80,
            height=20,
            font=("Courier", 12),
            bg="#2c3e50",
            fg="#ecf0f1",
            insertbackground="#ecf0f1"
        )
        self.texto_area.pack(fill="both", expand=True, pady=10)
        
        # Barra de estado
        self.status_bar = tk.Label(
            self.root,
            text="Listo para generar pirámides",
            relief="sunken",
            anchor="w",
            bg="#34495e",
            fg="white",
            font=("Arial", 10)
        )
        self.status_bar.pack(side="bottom", fill="x")
        
        # Generar una pirámide inicial
        self.generar_piramide()
    
    def crear_piramide(self, altura, estilo):
        """Genera una pirámide con la configuración especificada"""
        piramide = []
        
        for nivel in range(1, altura + 1):
            numeros = [str(random.randint(0, 9)) for _ in range(nivel)]
            espacios = " " * (altura - nivel)
            
            if estilo == "espaciado":
                linea = " ".join(numeros)
            else:
                linea = "".join(numeros)
            
            piramide.append(f"{espacios}{linea}")
        
        return "\n".join(piramide)
    
    def generar_piramide(self):
        """Genera y muestra una nueva pirámide"""
        try:
            altura = int(self.altura_var.get())
            estilo = self.estilo_var.get()
            
            if altura < 1 or altura > 15:
                messagebox.showerror("Error", "La altura debe estar entre 1 y 15")
                return
            
            piramide = self.crear_piramide(altura, estilo)
            
            # Actualizar fuente
            fuente = self.fuente_var.get()
            tamaño = int(self.tamaño_fuente_var.get())
            self.texto_area.config(font=(fuente, tamaño))
            
            # Agregar separador si ya hay contenido
            if self.texto_area.get("1.0", "end-1c"):
                self.texto_area.insert("end", "\n" + "="*50 + "\n")
            
            # Agregar nueva pirámide
            self.texto_area.insert("end", f"Pirámide {estilo} (altura: {altura})\n")
            self.texto_area.insert("end", "-" * 30 + "\n")
            self.texto_area.insert("end", piramide + "\n\n")
            
            # Scroll al final
            self.texto_area.see("end")
            
            # Actualizar status
            self.status_bar.config(text=f"Pirámide generada: altura {altura}, estilo {estilo}")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos")
    
    def generar_multiples(self):
        """Genera múltiples pirámides aleatorias"""
        try:
            if self.texto_area.get("1.0", "end-1c"):
                self.texto_area.insert("end", "\n" + "🔄 MÚLTIPLES PIRÁMIDES 🔄\n")
                self.texto_area.insert("end", "="*50 + "\n")
            
            for i in range(5):
                altura_aleatoria = random.randint(3, 8)
                estilo_aleatorio = random.choice(["espaciado", "compacto"])
                
                piramide = self.crear_piramide(altura_aleatoria, estilo_aleatorio)
                
                self.texto_area.insert("end", f"\nPirámide #{i+1} ({estilo_aleatorio}, altura: {altura_aleatoria})\n")
                self.texto_area.insert("end", "-" * 35 + "\n")
                self.texto_area.insert("end", piramide + "\n")
            
            self.texto_area.see("end")
            self.status_bar.config(text="5 pirámides múltiples generadas")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error generando múltiples pirámides: {str(e)}")
    
    def limpiar_texto(self):
        """Limpia el área de texto"""
        self.texto_area.delete("1.0", "end")
        self.status_bar.config(text="Área de texto limpiada")
    
    def copiar_texto(self):
        """Copia el contenido al portapapeles"""
        try:
            contenido = self.texto_area.get("1.0", "end-1c")
            if contenido.strip():
                self.root.clipboard_clear()
                self.root.clipboard_append(contenido)
                self.status_bar.config(text="Contenido copiado al portapapeles")
                messagebox.showinfo("Éxito", "Contenido copiado al portapapeles")
            else:
                messagebox.showwarning("Advertencia", "No hay contenido para copiar")
        except Exception as e:
            messagebox.showerror("Error", f"Error copiando al portapapeles: {str(e)}")

def main():
    root = tk.Tk()
    app = GeneradorPiramides(root)
    root.mainloop()

if __name__ == "__main__":
    main()