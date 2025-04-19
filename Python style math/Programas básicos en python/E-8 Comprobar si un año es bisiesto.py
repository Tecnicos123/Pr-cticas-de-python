def es_año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else: 
        return False
año = int(input("Ingrese un año: "))
if es_año_bisiesto(año):
    print("Año bisiesto")
else: 
    print("No es un año bisiesto")