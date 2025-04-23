import random
import string

def generar_contraseña(longitud, incluir_digitos=True, incluir_caracteres_especiales=True):
    caracteres = string.ascii_letters
    if incluir_digitos:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range (longitud))
    return contraseña

longitud_contraseña = 12
print("Contraseña generada: ", generar_contraseña(longitud_contraseña))