import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range (longitud))
    return contraseña

longitud_contraseña = 12

print("Contraseña generada: ", generar_contraseña(longitud_contraseña))