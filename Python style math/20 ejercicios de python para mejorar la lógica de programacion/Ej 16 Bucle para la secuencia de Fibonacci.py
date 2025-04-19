#Bibliografía pdf adjunto: guia-python-basica.pdf 

n1, n2 = 0, 1

print("Serie de Fibonacci para 10 números es: ")
for i in range(10):
    print(n1, end=", ")
    num = n1 + n2
    n1 = n2
    n2 = num