print("=== Calculador de Promedio de Notas ===\n")

while True:
    materia = input("Nombre de la materia (o 'salir' para terminar): ").strip()
    
    if materia.lower() == 'salir':
        print("¡👋!")
        break
    
    if not materia:
        print("❌ Debes ingresar un nombre de materia.\n")
        continue
    
    notas_str = input(f"Notas de {materia} (separadas por coma): ")
    
    try:
        notas = [float(nota.strip()) for nota in notas_str.split(",") if nota.strip()]
        
        if not notas:
            print("❌ No ingresaste notas válidas.\n")
            continue
            
        promedio = sum(notas) / len(notas)
        
        print("\n" + "="*40)
        print(f"📘 Materia: {materia}")
        print(f"📋 Notas: {notas}")
        print(f"📊 Promedio: {promedio:.2f}")
        
        if promedio < 3.0:
            print("❌ Fracasó la materia")
        else:
            print("✅ Aprobó la materia")
        print("="*40 + "\n")
           
    except ValueError:
        print("❌ Error: Ingresa solo números separados por comas.\n")