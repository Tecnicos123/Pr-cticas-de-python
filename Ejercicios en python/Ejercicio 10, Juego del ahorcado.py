import random

# Lista de palabras para adivinar
palabras = ["python", "programacion", "desarrollo", "inteligencia", "artificial", "algoritmo", "google"]

def seleccionar_palabra_al_azar():
    return random.choice(palabras)

def jugar():
    palabra = seleccionar_palabra_al_azar()
    palabra_oculta = "_" * len(palabra)
    intentos_maximos = 6
    intentos = 0
    letras_adivinadas = []

    print("¡Bienvenido al juego de Ahorcado!")
    print("Tienes que adivinar una palabra relacionada con la programación.")
    print("Tienes 6 intentos para adivinar la palabra.")

    while intentos < intentos_maximos:
        print("\nPalabra oculta: " + " ".join(palabra_oculta))
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has intentado con esa letra antes.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Correcto! La letra está en la palabra.")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta = palabra_oculta[:i] + letra + palabra_oculta[i+1:]
        else:
            print("¡Incorrecto! La letra no está en la palabra.")
            intentos += 1

        if palabra_oculta == palabra:
            print("\n¡Felicidades! Has adivinado la palabra: " + palabra)
            break

    if palabra_oculta != palabra:
        print("\n¡Oh no! Te has quedado sin intentos. La palabra era: " + palabra)

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo == "s":
        jugar()

jugar()

    
    
    
