import re

def es_direccion_email_valida(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

email_ingresado = input()
if es_direccion_email_valida(email_ingresado):
    print("Dirección de correo electrónico válida")
else:
    print("Dirección de correo electrónico inválida")