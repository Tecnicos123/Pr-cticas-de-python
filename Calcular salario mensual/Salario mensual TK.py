#Calculo de horas laboradas en el mes por la tarifa por hora mas décimo si lo hay
#EL propósito es obtener el salrio mensual mas el décimo, de haberlo
#Empleado 1 N B/2.77
#empleado 2 S B/2.91

import math

print ("Empleado No 1 N: ")
dias = float(input("Ingrese el numero de días laborados por el empleado 1 N: "))
horas = 8
costo = 2.77

decimo_emp_1 = int(input("Ingrese el monto del décimo_emp_1: "))
            
print ("Salario mensual del empleado 1 N: B/", "%.2f" % (dias*horas*costo))

salario_Emp_1 = (dias*horas*costo) + (decimo_emp_1)

print ("Empleado No 2 S: ")
dias = float(input("Ingrese el numero de días laborados por el empleado 2 S: "))
horas = 8
costo = 2.91

decimo_emp_2 = int(input("Ingrese el monto del décimo_emp_2: "))
            
print ("Salario mensual del empleado 2 S: B/", "%.2f" % (dias*horas*costo))

salario_Emp_2 = (dias*horas*costo) + (decimo_emp_2)

print ("Total de salario de los dos empledos N y S: ", "%.2f" % (salario_Emp_1 + salario_Emp_2))

Riesgos_Prof = (salario_Emp_1+salario_Emp_2)*float(0.0098)
Seguro_Edu = (salario_Emp_1+salario_Emp_2)*float(0.02159)
Seguro_Social = (salario_Emp_1+salario_Emp_2)*float(0.34056)

print ("Cuota mensual CSS: ", "%.2f" % (Riesgos_Prof+Seguro_Edu+Seguro_Social))

print("No hay mas empleados")
exit()
