def suma_de_digitos(n):
    return sum(int(digito) for digito in str(n))

numero = int(input("Ingrese un número: "))

print("Suma de los dígitos: ", suma_de_digitos(numero))