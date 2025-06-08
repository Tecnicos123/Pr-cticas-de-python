import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class CajeroAutomatico:
    def __init__(self):
        # Base de datos de clientes
        self.clientes = {
            "Juan": {"pin": "5249", "saldo": 1000.00},
            "Luis": {"pin": "2403", "saldo": 50.00},
            "Maria": {"pin": "0569", "saldo": 300.00}
        }
        
        self.cliente_actual = None
        self.intentos_pin = 0
        self.max_intentos = 3
        
        # Crear ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Cajero Automático")
        self.ventana.geometry("500x600")
        self.ventana.configure(bg="#2c3e50")
        self.ventana.resizable(False, False)
        
        # Centrar ventana
        self.centrar_ventana()
        
        # Inicializar interfaz
        self.crear_interfaz_login()
    
    def centrar_ventana(self):
        self.ventana.update_idletasks()
        x = (self.ventana.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (600 // 2)
        self.ventana.geometry(f"500x600+{x}+{y}")
    
    def limpiar_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    def crear_interfaz_login(self):
        self.limpiar_ventana()
        
        # Frame principal
        frame_principal = tk.Frame(self.ventana, bg="#2c3e50", padx=50, pady=50)
        frame_principal.pack(expand=True, fill="both")
        
        # Título
        titulo = tk.Label(frame_principal, text="🏧 CAJERO AUTOMÁTICO", 
                         font=("Arial", 24, "bold"), 
                         bg="#2c3e50", fg="#ecf0f1")
        titulo.pack(pady=(0, 30))
        
        # Subtítulo
        subtitulo = tk.Label(frame_principal, text="Ingrese sus credenciales", 
                           font=("Arial", 14), 
                           bg="#2c3e50", fg="#bdc3c7")
        subtitulo.pack(pady=(0, 30))
        
        # Frame para campos
        frame_campos = tk.Frame(frame_principal, bg="#2c3e50")
        frame_campos.pack(pady=20)
        
        # Usuario
        tk.Label(frame_campos, text="Usuario:", 
                font=("Arial", 12, "bold"), 
                bg="#2c3e50", fg="#ecf0f1").pack(anchor="w", pady=(0, 5))
        
        self.entry_usuario = tk.Entry(frame_campos, font=("Arial", 12), 
                                     width=25, relief="solid", bd=1)
        self.entry_usuario.pack(pady=(0, 15))
        
        # PIN
        tk.Label(frame_campos, text="PIN:", 
                font=("Arial", 12, "bold"), 
                bg="#2c3e50", fg="#ecf0f1").pack(anchor="w", pady=(0, 5))
        
        self.entry_pin = tk.Entry(frame_campos, font=("Arial", 12), 
                                 width=25, show="*", relief="solid", bd=1)
        self.entry_pin.pack(pady=(0, 20))
        
        # Botón de login
        btn_login = tk.Button(frame_campos, text="INGRESAR", 
                             font=("Arial", 12, "bold"), 
                             bg="#27ae60", fg="white", 
                             width=20, height=2,
                             relief="flat", cursor="hand2",
                             command=self.validar_credenciales)
        btn_login.pack(pady=10)
        
        # Información de usuarios (solo para demo)
        info_frame = tk.Frame(frame_principal, bg="#34495e", relief="solid", bd=1)
        info_frame.pack(pady=30, padx=20, fill="x")
        
        tk.Label(info_frame, text="Usuarios de prueba:", 
                font=("Arial", 10, "bold"), 
                bg="#34495e", fg="#ecf0f1").pack(pady=5)
        
        usuarios_info = "Juan (PIN: 5249) | Luis (PIN: 2403) | Maria (PIN: 0569)"
        tk.Label(info_frame, text=usuarios_info, 
                font=("Arial", 9), 
                bg="#34495e", fg="#bdc3c7").pack(pady=5)
        
        # Bind Enter key
        self.entry_pin.bind('<Return>', lambda e: self.validar_credenciales())
        self.entry_usuario.bind('<Return>', lambda e: self.entry_pin.focus())
        
        # Focus inicial
        self.entry_usuario.focus()
    
    def validar_credenciales(self):
        usuario = self.entry_usuario.get().strip()
        pin = self.entry_pin.get().strip()
        
        # Validar campos vacíos
        if not usuario or not pin:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return
        
        # Validar usuario existente
        if usuario not in self.clientes:
            self.intentos_pin += 1
            if self.intentos_pin >= self.max_intentos:
                messagebox.showerror("Bloqueado", "Demasiados intentos fallidos. Cajero bloqueado.")
                self.ventana.quit()
                return
            messagebox.showerror("Error", f"Usuario no encontrado. Intentos restantes: {self.max_intentos - self.intentos_pin}")
            self.entry_usuario.delete(0, tk.END)
            self.entry_pin.delete(0, tk.END)
            return
        
        # Validar PIN
        if self.clientes[usuario]["pin"] != pin:
            self.intentos_pin += 1
            if self.intentos_pin >= self.max_intentos:
                messagebox.showerror("Bloqueado", "Demasiados intentos fallidos. Cajero bloqueado.")
                self.ventana.quit()
                return
            messagebox.showerror("Error", f"PIN incorrecto. Intentos restantes: {self.max_intentos - self.intentos_pin}")
            self.entry_pin.delete(0, tk.END)
            return
        
        # Login exitoso
        self.cliente_actual = usuario
        self.intentos_pin = 0
        self.crear_menu_principal()
    
    def crear_menu_principal(self):
        self.limpiar_ventana()
        
        # Frame principal
        frame_principal = tk.Frame(self.ventana, bg="#2c3e50", padx=30, pady=30)
        frame_principal.pack(expand=True, fill="both")
        
        # Bienvenida
        bienvenida = tk.Label(frame_principal, 
                             text=f"¡Bienvenido/a, {self.cliente_actual}!", 
                             font=("Arial", 20, "bold"), 
                             bg="#2c3e50", fg="#ecf0f1")
        bienvenida.pack(pady=(0, 10))
        
        # Fecha y hora
        fecha_hora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        tk.Label(frame_principal, text=fecha_hora, 
                font=("Arial", 12), 
                bg="#2c3e50", fg="#bdc3c7").pack(pady=(0, 30))
        
        # Frame para botones
        frame_botones = tk.Frame(frame_principal, bg="#2c3e50")
        frame_botones.pack(expand=True)
        
        # Botones del menú
        botones = [
            ("💰 Estado de Cuenta", "#3498db", self.mostrar_estado_cuenta),
            ("💸 Retiro", "#e74c3c", self.realizar_retiro),
            ("💳 Depósito", "#27ae60", self.realizar_deposito),
            ("🚪 Salir", "#95a5a6", self.cerrar_sesion)
        ]
        
        for i, (texto, color, comando) in enumerate(botones):
            btn = tk.Button(frame_botones, text=texto, 
                           font=("Arial", 14, "bold"), 
                           bg=color, fg="white", 
                           width=20, height=3,
                           relief="flat", cursor="hand2",
                           command=comando)
            btn.pack(pady=15)
    
    def mostrar_estado_cuenta(self):
        saldo = self.clientes[self.cliente_actual]["saldo"]
        fecha_hora = datetime.now().strftime("%d/%m/%Y a las %H:%M:%S")
        
        mensaje = f"""
╔══════════════════════════════════╗
║         ESTADO DE CUENTA         ║
╠══════════════════════════════════╣
║ Cliente: {self.cliente_actual:<23} ║
║ Fecha: {fecha_hora:<25} ║
║ Saldo actual: B/ {saldo:>15.2f} ║
╚══════════════════════════════════╝
        """
        messagebox.showinfo("Estado de Cuenta", mensaje)
    
    def realizar_retiro(self):
        self.crear_ventana_transaccion("retiro")
    
    def realizar_deposito(self):
        self.crear_ventana_transaccion("deposito")
    
    def crear_ventana_transaccion(self, tipo):
        ventana_transaccion = tk.Toplevel(self.ventana)
        ventana_transaccion.title(f"{tipo.capitalize()}")
        ventana_transaccion.geometry("400x300")
        ventana_transaccion.configure(bg="#2c3e50")
        ventana_transaccion.resizable(False, False)
        ventana_transaccion.grab_set()  # Modal
        
        # Centrar ventana
        ventana_transaccion.update_idletasks()
        x = (ventana_transaccion.winfo_screenwidth() // 2) - (400 // 2)
        y = (ventana_transaccion.winfo_screenheight() // 2) - (300 // 2)
        ventana_transaccion.geometry(f"400x300+{x}+{y}")
        
        # Frame principal
        frame = tk.Frame(ventana_transaccion, bg="#2c3e50", padx=40, pady=40)
        frame.pack(expand=True, fill="both")
        
        # Título
        icono = "💸" if tipo == "retiro" else "💳"
        titulo = tk.Label(frame, text=f"{icono} {tipo.upper()}", 
                         font=("Arial", 18, "bold"), 
                         bg="#2c3e50", fg="#ecf0f1")
        titulo.pack(pady=(0, 20))
        
        # Saldo actual
        saldo_actual = self.clientes[self.cliente_actual]["saldo"]
        tk.Label(frame, text=f"Saldo actual: B/ {saldo_actual:.2f}", 
                font=("Arial", 12), 
                bg="#2c3e50", fg="#bdc3c7").pack(pady=(0, 20))
        
        # Campo de monto
        tk.Label(frame, text="Monto:", 
                font=("Arial", 12, "bold"), 
                bg="#2c3e50", fg="#ecf0f1").pack(anchor="w")
        
        entry_monto = tk.Entry(frame, font=("Arial", 14), 
                              width=15, justify="center", 
                              relief="solid", bd=1)
        entry_monto.pack(pady=(5, 20))
        entry_monto.focus()
        
        # Frame para botones
        frame_btn = tk.Frame(frame, bg="#2c3e50")
        frame_btn.pack()
        
        # Botón confirmar
        color = "#e74c3c" if tipo == "retiro" else "#27ae60"
        btn_confirmar = tk.Button(frame_btn, text="CONFIRMAR", 
                                 font=("Arial", 12, "bold"), 
                                 bg=color, fg="white", 
                                 width=12, height=2,
                                 relief="flat", cursor="hand2",
                                 command=lambda: self.procesar_transaccion(tipo, entry_monto.get(), ventana_transaccion))
        btn_confirmar.pack(side="left", padx=(0, 10))
        
        # Botón cancelar
        btn_cancelar = tk.Button(frame_btn, text="CANCELAR", 
                                font=("Arial", 12, "bold"), 
                                bg="#95a5a6", fg="white", 
                                width=12, height=2,
                                relief="flat", cursor="hand2",
                                command=ventana_transaccion.destroy)
        btn_cancelar.pack(side="left")
        
        # Bind Enter key
        entry_monto.bind('<Return>', lambda e: self.procesar_transaccion(tipo, entry_monto.get(), ventana_transaccion))
    
    def procesar_transaccion(self, tipo, monto_str, ventana):
        try:
            # Validar que sea un número
            monto = float(monto_str.replace(',', '.'))
            
            # Validar monto positivo
            if monto <= 0:
                messagebox.showerror("Error", "El monto debe ser mayor a cero")
                return
            
            # Validar decimales (máximo 2)
            if round(monto, 2) != monto:
                messagebox.showerror("Error", "El monto no puede tener más de 2 decimales")
                return
            
            saldo_actual = self.clientes[self.cliente_actual]["saldo"]
            
            if tipo == "retiro":
                # Validar fondos suficientes
                if monto > saldo_actual:
                    messagebox.showerror("Fondos Insuficientes", 
                                       f"No tiene fondos suficientes.\nSaldo disponible: B/ {saldo_actual:.2f}")
                    return
                
                # Procesar retiro
                nuevo_saldo = saldo_actual - monto
                self.clientes[self.cliente_actual]["saldo"] = nuevo_saldo
                
                mensaje = f"""
Retiro procesado exitosamente

Monto retirado: B/ {monto:.2f}
Saldo anterior: B/ {saldo_actual:.2f}
Saldo actual: B/ {nuevo_saldo:.2f}

¡Retire su dinero de la bandeja!
                """
                messagebox.showinfo("Retiro Exitoso", mensaje)
            
            else:  # depósito
                # Validar monto máximo por depósito
                if monto > 10000:
                    messagebox.showerror("Error", "El monto máximo por depósito es B/ 10,000.00")
                    return
                
                # Procesar depósito
                nuevo_saldo = saldo_actual + monto
                self.clientes[self.cliente_actual]["saldo"] = nuevo_saldo
                
                mensaje = f"""
Depósito procesado exitosamente

Monto depositado: B/ {monto:.2f}
Saldo anterior: B/ {saldo_actual:.2f}
Saldo actual: B/ {nuevo_saldo:.2f}
                """
                messagebox.showinfo("Depósito Exitoso", mensaje)
            
            ventana.destroy()
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un monto válido")
    
    def cerrar_sesion(self):
        respuesta = messagebox.askyesno("Cerrar Sesión", 
                                       "¿Está seguro que desea cerrar sesión?")
        if respuesta:
            self.cliente_actual = None
            messagebox.showinfo("Sesión Cerrada", "¡Gracias por usar nuestro cajero automático!")
            self.crear_interfaz_login()
    
    def ejecutar(self):
        self.ventana.mainloop()

# Ejecutar el cajero automático
if __name__ == "__main__":
    cajero = CajeroAutomatico()
    cajero.ejecutar()