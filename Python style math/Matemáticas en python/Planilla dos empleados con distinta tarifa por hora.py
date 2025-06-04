# Planilla dos empleados con distinta tarifa por hora
# los calculos se basan en los dias trabajados

empleados = {
    'N': 2.77,
    'S': 2.91,
    }

def calcular_pago(dias_trabajados, tarifa):
    """
    Calcula el pago total basado en los días trabajados y la tarifa por hora.
    """
    horas_por_dia = 8
    pago_total = dias_trabajados * horas_por_dia * tarifa
    return pago_total   

def calcular_sueldos():
    try:
        dias_N = float(input("Ingrese los días trabajados por el empleado N: "))
        dias_S = float(input("Ingrese los días trabajados por el empleado S: "))
        if dias_N < 0 or dias_S < 0:
            raise ValueError("Los días trabajados no pueden ser negativos.")
        pago_N = calcular_pago(dias_N, empleados['N'])
        pago_S = calcular_pago(dias_S, empleados['S'])
        print(f"Pago total del empleado N: ${pago_N:.2f}")
        print(f"Pago total del empleado S: ${pago_S:.2f}")
        Total_pago = pago_N + pago_S
        print(f"Total de pago de ambos empleados: ${Total_pago:.2f}")
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese un número válido de días trabajados.")
if __name__ == "__main__":
    calcular_sueldos()

# Este programa calcula el pago total de dos empleados con diferentes tarifas por hora
# basándose en los días trabajados. Se asegura de que los días ingresados sean válidos.
# Se utiliza un diccionario para almacenar las tarifas por hora de cada empleado.
# El programa maneja excepciones para evitar errores de entrada.
# El cálculo se realiza multiplicando los días trabajados por las horas diarias y la tarifa por hora.
# El resultado se muestra con dos decimales para mayor claridad.
# El programa es interactivo y solicita al usuario que ingrese los días trabajados.
# El uso de funciones mejora la organización del código y facilita su mantenimiento.
# El programa se ejecuta al llamar a la función calcular_sueldos.
# El uso de un diccionario permite una fácil modificación de las tarifas por hora si es necesario.