import random

def crear_piramide_numerica(altura=5):
    """
    Crea una pirámide de números aleatorios del 0 al 9
    
    Args:
        altura (int): Altura de la pirámide (número de niveles)
    """
    print(f"Pirámide de números aleatorios (altura: {altura})")
    print("-" * 40)
    
    for nivel in range(1, altura + 1):
        # Generar números aleatorios para este nivel
        numeros = [str(random.randint(0, 9)) for _ in range(nivel)]
        
        # Calcular espacios para centrar la pirámide
        espacios = " " * (altura - nivel)
        
        # Unir números con espacios entre ellos
        linea_numeros = " ".join(numeros)
        
        # Imprimir el nivel centrado
        print(f"{espacios}{linea_numeros}")

def crear_piramide_compacta(altura=7):
    """
    Crea una pirámide más compacta sin espacios entre números
    """
    print(f"\nPirámide compacta (altura: {altura})")
    print("-" * 40)
    
    for nivel in range(1, altura + 1):
        # Generar números aleatorios para este nivel
        numeros = "".join([str(random.randint(0, 9)) for _ in range(nivel)])
        
        # Calcular espacios para centrar
        espacios = " " * (altura - nivel)
        
        # Imprimir el nivel centrado
        print(f"{espacios}{numeros}")

def crear_piramide_personalizada():
    """
    Permite al usuario personalizar la pirámide
    """
    try:
        altura = int(input("\n¿Qué altura quieres para tu pirámide? (1-15): "))
        if altura < 1 or altura > 15:
            print("La altura debe estar entre 1 y 15")
            return
        
        estilo = input("¿Qué estilo prefieres? (1: espaciado, 2: compacto): ")
        
        print(f"\nTu pirámide personalizada:")
        print("-" * 40)
        
        for nivel in range(1, altura + 1):
            numeros = [str(random.randint(0, 9)) for _ in range(nivel)]
            espacios = " " * (altura - nivel)
            
            if estilo == "1":
                linea = " ".join(numeros)
            else:
                linea = "".join(numeros)
            
            print(f"{espacios}{linea}")
            
    except ValueError:
        print("Por favor, ingresa un número válido")

# Demostración del programa
if __name__ == "__main__":
    # Establecer semilla para reproducibilidad (opcional)
    # random.seed(42)
    
    # Crear diferentes tipos de pirámides
    crear_piramide_numerica(5)
    crear_piramide_compacta(6)
    
    # Ejemplo de múltiples pirámides
    print("\n" + "="*50)
    print("MÚLTIPLES PIRÁMIDES ALEATORIAS")
    print("="*50)
    
    for i in range(3):
        print(f"\nPirámide #{i+1}:")
        crear_piramide_numerica(4)
    
    # Opción interactiva (descomenta para usar)
    # crear_piramide_personalizada()