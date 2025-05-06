
import random
import tkinter as tk
from tkinter import ttk
import time

class LuckyNumbersApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Números de la Suerte")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Estilo
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
        self.style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
        self.style.configure("Title.TLabel", font=("Arial", 16, "bold"), background="#f0f0f0")
        self.style.configure("Result.TLabel", font=("Arial", 24, "bold"), background="#f0f0f0")
        
        # Marco principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, text="🍀 Generador de Números de la Suerte 🍀", style="Title.TLabel")
        title_label.pack(pady=10)
        
        # Marco para número de dos dígitos
        two_digit_frame = tk.LabelFrame(main_frame, text="Número de la Suerte (00-99)", font=("Arial", 12), bg="#f0f0f0")
        two_digit_frame.pack(pady=15, fill="x")
        
        self.two_digit_label = ttk.Label(two_digit_frame, text="--", style="Result.TLabel")
        self.two_digit_label.pack(pady=10)
        
        self.two_digit_button = ttk.Button(two_digit_frame, text="Generar Número de la Suerte", command=self.generate_two_digit)
        self.two_digit_button.pack(pady=10)
        
        # Marco para billete de cuatro dígitos
        four_digit_frame = tk.LabelFrame(main_frame, text="Billete de la Suerte (0000-9999)", font=("Arial", 12), bg="#f0f0f0")
        four_digit_frame.pack(pady=15, fill="x")
        
        self.four_digit_label = ttk.Label(four_digit_frame, text="----", style="Result.TLabel")
        self.four_digit_label.pack(pady=10)
        
        self.four_digit_button = ttk.Button(four_digit_frame, text="Generar Billete de la Suerte", command=self.generate_four_digit)
        self.four_digit_button.pack(pady=10)
        
        # Botón para generar ambos
        generate_all_button = ttk.Button(main_frame, text="¡Generar Todos los Números!", command=self.generate_all)
        generate_all_button.pack(pady=20)
        
        # Fecha y hora
        self.date_label = ttk.Label(main_frame, text=self.get_date(), style="TLabel")
        self.date_label.pack(pady=10)
        
    def generate_two_digit(self):
        # Efecto de "ruleta"
        for i in range(10):
            num = str(random.randint(0, 99)).zfill(2)
            self.two_digit_label.config(text=num)
            self.root.update()
            time.sleep(0.1)
        
        # Número final
        lucky_number = str(random.randint(0, 99)).zfill(2)
        self.two_digit_label.config(text=lucky_number)
        
    def generate_four_digit(self):
        # Efecto de "ruleta"
        for i in range(10):
            num = str(random.randint(0, 9999)).zfill(4)
            self.four_digit_label.config(text=num)
            self.root.update()
            time.sleep(0.1)
        
        # Número final
        lucky_ticket = str(random.randint(0, 9999)).zfill(4)
        self.four_digit_label.config(text=lucky_ticket)
    
    def generate_all(self):
        self.generate_two_digit()
        self.generate_four_digit()
    
    def get_date(self):
        return time.strftime("Fecha: %d/%m/%Y - Hora: %H:%M:%S")
    
    def update_date(self):
        self.date_label.config(text=self.get_date())
        self.root.after(1000, self.update_date)

if __name__ == "__main__":
    root = tk.Tk()
    app = LuckyNumbersApp(root)
    app.update_date()
    root.mainloop()