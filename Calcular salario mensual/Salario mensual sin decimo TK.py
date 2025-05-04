#Calculo de horas laboradas en el mes por la tarifa por hora
#EL propósito es obtener el salrio mensual
#Empleado 1 N B/2.77
#empleado 2 S B/2.91

import math


print ("Empleado No 1 N: ")
dias = float(input("Ingrese el numero de días laborados: "))
horas = 8
costo = 2.77
            
print ("Salario mensual: B/", "%.2f" % (dias*horas*costo))

salario_Emp_1 = (dias*horas*costo)

print ("Empleado No 2 S: ")
dias = float(input("Ingrese el numero de días laborados: "))
horas = 8
costo = 2.91
            
print ("Salario mensual: B/", "%.2f" % (dias*horas*costo))

salario_Emp_2 = (dias*horas*costo)

print ("Total de salario de los dos empledos: ", "%.2f" % (salario_Emp_1 + salario_Emp_2))

Riesgos_Prof = (salario_Emp_1+salario_Emp_2)*float(0.0098)
Seguro_Edu = (salario_Emp_1+salario_Emp_2)*float(0.0275)
Seguro_Social = (salario_Emp_1+salario_Emp_2)*float(0.36656)

print ("Cuota mensual CSS: ", "%.2f" % (Riesgos_Prof+Seguro_Edu+Seguro_Social))

print("No hay mas empleados")
