#Bibliografía pdf adjunto: guia-python-basica.pdf 

texto = "Antonio Richaud"

conteos = {}

for char in texto:
    if char in conteos:
        conteos[char] += 1
    else:
        conteos[char] = 1

print(conteos)