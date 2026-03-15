import random

def gerar_historia(tema):

    ideias = [
        "uma aventura épica",
        "uma história de sobrevivência",
        "um mistério futurista",
        "uma jornada emocionante",
        "um universo cheio de magia"
    ]

    historia = f"Este filme conta {random.choice(ideias)} sobre {tema}."

    return historia
