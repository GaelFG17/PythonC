import random

def obtener_eleccion_usuario():
    eleccion_usuario = input("Ingresa tu elección (piedra, papel, tijeras): ").lower()
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Elección inválida. Por favor ingresa piedra, papel o tijeras: ").lower()
    return eleccion_usuario

def obtener_eleccion_computadora():
    return random.choice(["piedra", "papel", "tijeras"])

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "¡Es un empate!"
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or \
         (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_usuario == "tijeras" and eleccion_computadora == "papel"):
        return "¡Tú ganas!"
    else:
        return "¡Tú pierdes!"

def jugar():
    eleccion_usuario = obtener_eleccion_usuario()
    eleccion_computadora = obtener_eleccion_computadora()
    print(f"Tú elegiste: {eleccion_usuario}")
    print(f"La computadora eligió: {eleccion_computadora}")
    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
    print(resultado)

if __name__ == "__main__":
    jugar()