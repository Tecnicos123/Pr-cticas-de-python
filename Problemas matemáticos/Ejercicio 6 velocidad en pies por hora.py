"""
Una bola de boliche se lanza a una velocidad de 430 m/s,
se desea calcular esta velocidad en pies por hora.
"""

# Datos
velocidad_ms = 430  # metros por segundo

# Factores de conversión
metros_a_pies = 3.28084     # 1 metro ≈ 3.28084 pies
segundos_a_horas = 3600     # 1 hora = 3600 segundos

# Cálculo
velocidad_pies_por_hora = velocidad_ms * metros_a_pies * segundos_a_horas

print("=== CONVERSIÓN DE VELOCIDAD ===")
print(f"Velocidad:          {velocidad_ms} m/s")
print(f"Velocidad en pies/hora: {velocidad_pies_por_hora:,.0f} ft/h")