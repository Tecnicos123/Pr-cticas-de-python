#Calculo de horas laboradas en el mes por la tarifa por hora
#EL propósito es obtener el salrio mensual
#Empleado 1 N B/2.77
#empleado 2 S B/2.91

def calcular_salario(dias_laborados, costo_hora, horas_diarias=8):
    """
    Calcula el salario mensual de un empleado.
    
    Args:
        dias_laborados (float): Número de días trabajados
        costo_hora (float): Costo por hora trabajada
        horas_diarias (int, opcional): Horas trabajadas por día, por defecto 8
    
    Returns:
        float: Salario mensual calculado
    """
    return dias_laborados * horas_diarias * costo_hora

def calcular_cuotas_css(salario_total, decimo):
    """
    Calcula las cuotas del CSS incluyendo el décimo.
    
    Args:
        salario_total (float): Suma de los salarios
        decimo (float): Monto del décimo
    
    Returns:
        dict: Diccionario con los valores de cada cuota y el total
    """
    base_calculo = salario_total + decimo
    riesgos_prof = base_calculo * 0.0098
    seguro_edu = base_calculo * 0.0275
    seguro_social = base_calculo * 0.24388
    total = riesgos_prof + seguro_edu + seguro_social
    
    return {
        'riesgos_prof': riesgos_prof,
        'seguro_edu': seguro_edu,
        'seguro_social': seguro_social,
        'total': total
    }

def imprimir_resultados(salarios, cuotas, decimo):
    """
    Imprime los resultados formateados.
    
    Args:
        salarios (dict): Diccionario con los salarios calculados
        cuotas (dict): Diccionario con las cuotas del CSS
        decimo (float): Monto del décimo
    """
    print("\n===== RESUMEN =====")
    for nombre, salario in salarios.items():
        print(f"Salario mensual de {nombre}: B/ {salario:.2f}")
    
    print(f"\nTotal de salarios: B/ {sum(salarios.values()):.2f}")
    print(f"Total del décimo: B/ {decimo:.2f}")
    
    print("\n===== CUOTAS CSS =====")
    print(f"Riesgos Profesionales: B/ {cuotas['riesgos_prof']:.2f}")
    print(f"Seguro Educativo: B/ {cuotas['seguro_edu']:.2f}")
    print(f"Seguro Social: B/ {cuotas['seguro_social']:.2f}")
    print(f"Cuota mensual total CSS (incluyendo décimo): B/ {cuotas['total']:.2f}")

def main():
    """Función principal que ejecuta el programa"""
    salarios = {}
    
    # Empleado 1
    print("===== Empleado No 1 (N) =====")
    dias = float(input("Ingrese el número de días laborados: "))
    costo = 2.77
    salario_emp_1 = calcular_salario(dias, costo)
    print(f"Salario mensual: B/ {salario_emp_1:.2f}")
    salarios["Empleado N"] = salario_emp_1
    
    # Empleado 2
    print("\n===== Empleado No 2 (S) =====")
    dias = float(input("Ingrese el número de días laborados: "))
    costo = 2.91
    salario_emp_2 = calcular_salario(dias, costo)
    print(f"Salario mensual: B/ {salario_emp_2:.2f}")
    salarios["Empleado S"] = salario_emp_2
    
    # Décimo
    decimo = float(input("\nIngrese el monto total del décimo de los dos empleados: B/ "))
    
    # Calcular cuotas CSS
    cuotas = calcular_cuotas_css(sum(salarios.values()), decimo)
    
    # Mostrar resultados
    imprimir_resultados(salarios, cuotas, decimo)
    
    print("\nNo hay más empleados")

if __name__ == "__main__":
    main()