import tkinter as tk
from tkinter import ttk


def dinero(n):
    """Da formato de dinero: 1234.5 -> $1,234.50"""
    return f"${n:,.2f}"


class CalculadoraPrecio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de precio")
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        # Variables ligadas a los campos de texto
        self.var_precio = tk.StringVar()
        self.var_impuesto = tk.StringVar()
        self.var_descuento = tk.StringVar()
        self.var_mensaje = tk.StringVar()

        self.crear_widgets()

    def crear_widgets(self):
        ttk.Label(self, text="Calculadora de precio",
                  font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=(0, 12))

        # Paso 1: precio e impuesto en un mismo renglón
        ttk.Label(self, text="Precio del producto").grid(row=1, column=0, sticky="w")
        ttk.Label(self, text="Impuesto (%)").grid(row=1, column=1, sticky="w", padx=10)

        self.entry_precio = ttk.Entry(self, textvariable=self.var_precio, width=15)
        self.entry_precio.grid(row=2, column=0)
        self.entry_impuesto = ttk.Entry(self, textvariable=self.var_impuesto, width=15)
        self.entry_impuesto.grid(row=2, column=1, padx=10)
        ttk.Button(self, text="Siguiente", command=self.paso_siguiente).grid(row=2, column=2)

        # Paso 2: descuento (aparece después del paso 1)
        self.frame_descuento = ttk.Frame(self)
        self.frame_descuento.grid(row=3, column=0, columnspan=3, sticky="w", pady=(12, 0))
        ttk.Label(self.frame_descuento,
                  text="Descuento por promoción (%)").grid(row=0, column=0, sticky="w")
        self.entry_descuento = ttk.Entry(self.frame_descuento,
                                         textvariable=self.var_descuento, width=15)
        self.entry_descuento.grid(row=1, column=0)
        ttk.Button(self.frame_descuento, text="Calcular",
                   command=self.calcular).grid(row=1, column=1, padx=10)
        self.frame_descuento.grid_remove()  # oculto al inicio

        # Mensaje de error
        ttk.Label(self, textvariable=self.var_mensaje,
                  foreground="#b91c1c").grid(row=4, column=0, columnspan=3, sticky="w", pady=6)

        # Resultados
        self.frame_resultado = ttk.Frame(self)
        self.frame_resultado.grid(row=5, column=0, columnspan=3, sticky="ew")
        self.frame_resultado.grid_remove()

        self.etiquetas = []  # (texto, valor) de cada fila
        for i in range(5):
            texto = ttk.Label(self.frame_resultado)
            valor = ttk.Label(self.frame_resultado)
            texto.grid(row=i, column=0, sticky="w", pady=3)
            valor.grid(row=i, column=1, sticky="e", pady=3, padx=(40, 0))
            self.etiquetas.append((texto, valor))
        self.frame_resultado.columnconfigure(1, weight=1)

        # La última fila (precio a pagar) se resalta
        for lbl in self.etiquetas[-1]:
            lbl.configure(font=("Arial", 11, "bold"), foreground="#15803d")

        self.entry_precio.focus()

    def paso_siguiente(self):
        """Valida precio e impuesto y muestra el campo de descuento."""
        self.frame_resultado.grid_remove()
        try:
            precio = float(self.var_precio.get())
            impuesto = float(self.var_impuesto.get())
            if precio < 0 or impuesto < 0:
                raise ValueError
        except ValueError:
            self.var_mensaje.set("Escribe un precio y un impuesto válidos (números ≥ 0).")
            self.frame_descuento.grid_remove()
            return

        self.var_mensaje.set("")
        self.frame_descuento.grid()
        self.entry_descuento.focus()

    def calcular(self):
        """Calcula y muestra los resultados."""
        try:
            precio = float(self.var_precio.get())
            impuesto = float(self.var_impuesto.get())
            descuento = float(self.var_descuento.get())
            if not 0 <= descuento <= 100:
                raise ValueError
        except ValueError:
            self.var_mensaje.set("El descuento debe ser un número entre 0 y 100.")
            self.frame_resultado.grid_remove()
            return

        self.var_mensaje.set("")

        # Cálculos
        monto_impuesto = precio * impuesto / 100
        precio_con_impuesto = precio + monto_impuesto
        monto_descuento = precio_con_impuesto * descuento / 100
        precio_final = precio_con_impuesto - monto_descuento

        filas = [
            ("Precio de lista", dinero(precio)),
            (f"Impuesto ({impuesto:g}%)", "+ " + dinero(monto_impuesto)),
            ("Precio + impuesto", dinero(precio_con_impuesto)),
            (f"Descuento ({descuento:g}%)", "- " + dinero(monto_descuento)),
            ("PRECIO A PAGAR", dinero(precio_final)),
        ]
        for (lbl_texto, lbl_valor), (texto, valor) in zip(self.etiquetas, filas):
            lbl_texto.configure(text=texto)
            lbl_valor.configure(text=valor)

        self.frame_resultado.grid()


if __name__ == "__main__":
    CalculadoraPrecio().mainloop()
