import random

def generate_random_quote():
    quotes = [
        "La mejor manera de predecir el futuro es inventarlo. - Alan Kay",
        "La vida es 10% lo que nos sucede y 90% cómo reaccionamos a ello. - Charles R. Swindoll",
        "La única manera de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
        "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. - Albert Schweitzer",
        "Tu tiempo es limitado, no lo desperdicies viviendo la vida de alguien más. - Steve Jobs"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print(generate_random_quote())