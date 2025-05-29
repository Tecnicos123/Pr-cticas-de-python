import tkinter as tk
from tkinter import messagebox
import random

# Variables globales
secret_number = random.randint(1, 20)
attempts_left = 5

# Función para verificar la suposición
def check_guess():
    global attempts_left
    guess = entry.get()

    try:
        guess = int(guess)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return

    if guess < 1 or guess > 20:
        messagebox.showwarning("Fuera de rango", "El número debe estar entre 1 y 20.")
        return

    attempts_left -= 1

    if guess < secret_number:
        result.set(f"{guess} es menor que el número secreto.")
    elif guess > secret_number:
        result.set(f"{guess} es mayor que el número secreto.")
    else:
        result.set(f"¡Correcto! El número secreto era {secret_number}.")
        end_game()
        return

    if attempts_left == 0:
        messagebox.showinfo("Fin del juego", f"Has agotado tus intentos. El número era {secret_number}.")
        end_game()
    else:
        attempts_label.config(text=f"Intentos restantes: {attempts_left}")

# Función para reiniciar el juego
def reset_game():
    global secret_number, attempts_left
    secret_number = random.randint(1, 20)
    attempts_left = 5
    entry.config(state='normal')
    guess_button.config(state='normal')
    entry.delete(0, tk.END)
    result.set("")
    attempts_label.config(text=f"Intentos restantes: {attempts_left}")

# Función para finalizar el juego (desactiva entrada y botón)
def end_game():
    entry.config(state='disabled')
    guess_button.config(state='disabled')

# Crear la interfaz
root = tk.Tk()
root.title("Adivina el número")

tk.Label(root, text="Adivina el número entre 1 y 20:").pack()

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Adivinar", command=check_guess)
guess_button.pack()

reset_button = tk.Button(root, text="Reiniciar", command=reset_game)
reset_button.pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

attempts_label = tk.Label(root, text=f"Intentos restantes: {attempts_left}")
attempts_label.pack()

root.mainloop()
