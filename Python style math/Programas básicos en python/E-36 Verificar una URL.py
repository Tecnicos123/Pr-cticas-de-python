import re

def es_url_valida(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http://, https://, ftp://, ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # dominio
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...o dirección IP
        r'(?::\d+)?'  # puerto opcional
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # ruta y/o parámetros de consulta
    return re.match(regex, url) is not None

input_url = input("Ingrese una URL: ")
if es_url_valida(input_url):
    print("URL válida")
else:
    print("URL inválida")