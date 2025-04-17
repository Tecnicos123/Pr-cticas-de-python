#funcion para verificar si la lista esta vacía

def es_lista_vacia(lista):
    return len(lista) == 0

mi_lista = []

print(f"¿La lista está vacía? {es_lista_vacia(mi_lista)}")