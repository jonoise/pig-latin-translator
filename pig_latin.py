# Pig latin translator.

def de_humano_a_pig_latin(text):
    palabras = text.split(' ')
    final = []
    for palabra in palabras:
        traducida = palabra + f'{palabra[0]}ay'
        final.append(traducida[1:])
    return " ".join(final)
        
def de_pig_latin_a_humano(text):
    palabras = text.split(' ')
    final = []
    for palabra in palabras:
        traducida = palabra[-3:-2] + palabra[:-3]
        final.append(traducida)
    return " ".join(final)