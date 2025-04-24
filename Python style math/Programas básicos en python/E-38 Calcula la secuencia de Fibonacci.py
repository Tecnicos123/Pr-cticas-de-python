nterms = int(input("¿Cuántos términos? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Por favor, ingrese un número entero positivo")
elif nterms == 1:
    print("Secuencia de Fibonacci hasta", nterms, ":")
    print(n1)
else:
    print("Secuencia de Fibonacci: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1