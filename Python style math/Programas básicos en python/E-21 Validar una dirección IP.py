import socket

def es_direccion_ip_valida(ip):

    try:

        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
direccion_ip = input("Ingrese una dirección IP: ")
if es_direccion_ip_valida(direccion_ip):
    print("Dirección IP válida")
    