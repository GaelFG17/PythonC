import random

def adivina_el_numero():
    numero_a_adivinar = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al Juego de Adivinar el Número!")
    print("He seleccionado un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))
            intentos += 1

            if adivinanza < numero_a_adivinar:
                print("¡Demasiado bajo! Inténtalo de nuevo.")
            elif adivinanza > numero_a_adivinar:
                print("¡Demasiado alto! Inténtalo de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido.")

if __name__ == "__main__":
    adivina_el_numero()