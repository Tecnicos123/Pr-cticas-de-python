# Calcular el salario de un empleado
# Fórmula: salario = horas_trabajadas * tarifa_hora

horas = input("Ingrese las horas trabajadas: ")
tarifa = input("Ingrese el costo por hora: ")
sueldo = float(horas) * float(tarifa)
print(f"El salario es: ${sueldo:.2f}")

# Versión mejorada con validación de datos
try:
    horas = float(input("Ingrese las horas trabajadas: "))
    tarifa = float(input("Ingrese el costo por hora: "))
    
    # Validar que los valores sean positivos
    if horas < 0 or tarifa < 0:
        print("Error: Las horas y la tarifa deben ser valores positivos")
    else:
        sueldo = horas * tarifa
        print(f"El salario es: ${sueldo:.2f}")

except ValueError:
    print("Error: Por favor ingrese valores numéricos válidos")
