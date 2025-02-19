#Calculo de horas laboradas en el mes por la tarifa por hora
#EL propósito es obtener el salrio mensual
#Empleado 1 N B/2.77
#empleado 2 S B/2.91

print("Empleado No 1 N: ")
dias= float(input("Ingrese el numero de días laborados: "))
horas= 8
costo= 2.77
            
print ("Salario mensual: B/", (dias*horas*costo))

print("Empleado No 2 S: ")
dias= float(input("Ingrese el numero de días laborados: "))
horas= 8
costo= 2.91
            
print ("Salario mensual: B/", (dias*horas*costo))

print("Otro empleado")

nombre= (input("Ingrese en nombre del empleado: "))
dias= float(input("Ingrese el numero de días laborados: "))
horas= float(input("Ingrese el número de horas por dia: "))
costo= float(input("Ingrese el costo por hora: "))
            
print ("Nombre: ", nombre)
print ("Salario mensual: B/", (dias*horas*costo))

print("No hay mas empleados")
exit()








