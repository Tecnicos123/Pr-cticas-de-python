import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import time
import re
from collections import Counter

class AnalizadorLectura:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Lectura con Cronómetro")
        self.root.geometry("800x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variables para el cronómetro
        self.tiempo_inicio = None
        self.tiempo_fin = None
        self.cronometro_activo = False
        
        # Configurar la interfaz
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar el grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        titulo = tk.Label(main_frame, text="📚 Analizador de Lectura", 
                         font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Frame para el cronómetro
        cronometro_frame = ttk.LabelFrame(main_frame, text="⏱️ Cronómetro", padding="10")
        cronometro_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.tiempo_label = tk.Label(cronometro_frame, text="00:00:00", 
                                    font=("Arial", 20, "bold"), fg='#e74c3c')
        self.tiempo_label.grid(row=0, column=0, padx=10)
        
        self.btn_iniciar = tk.Button(cronometro_frame, text="▶️ Iniciar", 
                                    command=self.iniciar_cronometro, bg='#27ae60', fg='white',
                                    font=("Arial", 10, "bold"))
        self.btn_iniciar.grid(row=0, column=1, padx=5)
        
        self.btn_detener = tk.Button(cronometro_frame, text="⏹️ Detener", 
                                    command=self.detener_cronometro, bg='#e74c3c', fg='white',
                                    font=("Arial", 10, "bold"))
        self.btn_detener.grid(row=0, column=2, padx=5)
        
        self.btn_reiniciar = tk.Button(cronometro_frame, text="🔄 Reiniciar", 
                                      command=self.reiniciar_cronometro, bg='#f39c12', fg='white',
                                      font=("Arial", 10, "bold"))
        self.btn_reiniciar.grid(row=0, column=3, padx=5)
        
        # Área de texto para la lectura
        texto_frame = ttk.LabelFrame(main_frame, text="📝 Texto de Lectura", padding="10")
        texto_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        texto_frame.columnconfigure(0, weight=1)
        texto_frame.rowconfigure(0, weight=1)
        
        self.texto_area = scrolledtext.ScrolledText(texto_frame, height=8, width=70, 
                                                   font=("Arial", 11), wrap=tk.WORD)
        self.texto_area.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Botón para analizar
        self.btn_analizar = tk.Button(main_frame, text="📊 Analizar Lectura", 
                                     command=self.analizar_texto, bg='#3498db', fg='white',
                                     font=("Arial", 12, "bold"), pady=5)
        self.btn_analizar.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Frame para resultados
        resultados_frame = ttk.LabelFrame(main_frame, text="📈 Resultados del Análisis", padding="10")
        resultados_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        resultados_frame.columnconfigure(0, weight=1)
        resultados_frame.rowconfigure(1, weight=1)
        
        # Estadísticas
        self.stats_label = tk.Label(resultados_frame, text="", font=("Arial", 10), 
                                   justify=tk.LEFT, bg='#ecf0f1', relief=tk.RAISED, padx=10, pady=5)
        self.stats_label.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Lista de palabras ordenadas
        palabras_frame = ttk.Frame(resultados_frame)
        palabras_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        palabras_frame.columnconfigure(0, weight=1)
        palabras_frame.rowconfigure(0, weight=1)
        
        tk.Label(palabras_frame, text="📋 Palabras ordenadas alfabéticamente:", 
                font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W)
        
        self.palabras_listbox = tk.Listbox(palabras_frame, height=8, font=("Arial", 9))
        scrollbar = ttk.Scrollbar(palabras_frame, orient=tk.VERTICAL, command=self.palabras_listbox.yview)
        self.palabras_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.palabras_listbox.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        
        # Configurar pesos para redimensionamiento
        main_frame.rowconfigure(2, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Inicializar cronómetro
        self.actualizar_cronometro()
        
    def iniciar_cronometro(self):
        if not self.cronometro_activo:
            self.tiempo_inicio = time.time()
            self.cronometro_activo = True
            self.btn_iniciar.config(state=tk.DISABLED)
            self.btn_detener.config(state=tk.NORMAL)
            
    def detener_cronometro(self):
        if self.cronometro_activo:
            self.tiempo_fin = time.time()
            self.cronometro_activo = False
            self.btn_iniciar.config(state=tk.NORMAL)
            self.btn_detener.config(state=tk.DISABLED)
            
    def reiniciar_cronometro(self):
        self.cronometro_activo = False
        self.tiempo_inicio = None
        self.tiempo_fin = None
        self.tiempo_label.config(text="00:00:00")
        self.btn_iniciar.config(state=tk.NORMAL)
        self.btn_detener.config(state=tk.DISABLED)
        
    def actualizar_cronometro(self):
        if self.cronometro_activo and self.tiempo_inicio:
            tiempo_actual = time.time() - self.tiempo_inicio
            horas = int(tiempo_actual // 3600)
            minutos = int((tiempo_actual % 3600) // 60)
            segundos = int(tiempo_actual % 60)
            tiempo_str = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.tiempo_label.config(text=tiempo_str)
        
        # Programar la siguiente actualización
        self.root.after(1000, self.actualizar_cronometro)
        
    def limpiar_texto(self, texto):
        # Convertir a minúsculas y eliminar signos de puntuación
        texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
        palabras = texto_limpio.split()
        return [palabra for palabra in palabras if palabra]
        
    def calcular_velocidad_lectura(self, num_palabras, tiempo_segundos):
        if tiempo_segundos == 0:
            return 0, "Sin tiempo registrado"
        
        # Palabras por minuto
        ppm = (num_palabras / tiempo_segundos) * 60
        
        # Clasificación de velocidad de lectura
        if ppm < 200:
            clasificacion = "🐌 Lenta"
            color = "#e74c3c"
        elif ppm < 300:
            clasificacion = "👍 Normal"
            color = "#f39c12"
        elif ppm < 400:
            clasificacion = "🚀 Rápida"
            color = "#27ae60"
        else:
            clasificacion = "⚡ Muy Rápida"
            color = "#8e44ad"
            
        return ppm, clasificacion, color
        
    def analizar_texto(self):
        texto = self.texto_area.get("1.0", tk.END).strip()
        
        if not texto:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un texto para analizar.")
            return
            
        # Limpiar y procesar el texto
        palabras = self.limpiar_texto(texto)
        
        if not palabras:
            messagebox.showwarning("Advertencia", "No se encontraron palabras válidas en el texto.")
            return
            
        # Contar palabras
        num_palabras = len(palabras)
        palabras_unicas = len(set(palabras))
        contador_palabras = Counter(palabras)
        
        # Ordenar palabras alfabéticamente
        palabras_ordenadas = sorted(set(palabras))
        
        # Calcular tiempo de lectura
        tiempo_lectura = 0
        if self.tiempo_inicio and self.tiempo_fin:
            tiempo_lectura = self.tiempo_fin - self.tiempo_inicio
        elif self.tiempo_inicio and self.cronometro_activo:
            tiempo_lectura = time.time() - self.tiempo_inicio
            
        # Calcular velocidad de lectura
        if tiempo_lectura > 0:
            ppm, clasificacion, color = self.calcular_velocidad_lectura(num_palabras, tiempo_lectura)
            tiempo_str = f"{int(tiempo_lectura//60):02d}:{int(tiempo_lectura%60):02d}"
            velocidad_info = f"⏱️ Tiempo: {tiempo_str} | 📊 Velocidad: {ppm:.1f} PPM | {clasificacion}"
        else:
            velocidad_info = "⏱️ Tiempo: No registrado | Use el cronómetro para medir la velocidad"
            color = "#7f8c8d"
            
        # Mostrar estadísticas
        stats_text = f"""📊 ESTADÍSTICAS DE LECTURA 📊

📝 Total de palabras: {num_palabras}
🔤 Palabras únicas: {palabras_unicas}
📈 Diversidad léxica: {(palabras_unicas/num_palabras)*100:.1f}%

{velocidad_info}

🏆 Palabra más frecuente: "{contador_palabras.most_common(1)[0][0]}" ({contador_palabras.most_common(1)[0][1]} veces)"""
        
        self.stats_label.config(text=stats_text, fg=color if 'color' in locals() else '#2c3e50')
        
        # Llenar la lista de palabras ordenadas
        self.palabras_listbox.delete(0, tk.END)
        for i, palabra in enumerate(palabras_ordenadas, 1):
            frecuencia = contador_palabras[palabra]
            self.palabras_listbox.insert(tk.END, f"{i:3d}. {palabra} ({frecuencia} veces)")
            
        messagebox.showinfo("Análisis Completo", 
                           f"✅ Análisis completado exitosamente!\n\n"
                           f"Se encontraron {num_palabras} palabras en total.\n"
                           f"Se identificaron {palabras_unicas} palabras únicas.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorLectura(root)
    root.mainloop()