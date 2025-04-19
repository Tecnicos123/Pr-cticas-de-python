#Bibliografía pdf adjunto: guia-python-basica.pdf 

for i in  range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("Tres y Cinco")
    elif i % 3 == 0:
        print("Tres")
    elif i % 5 == 0:
        print("Cinco")
    else:
        print(i)