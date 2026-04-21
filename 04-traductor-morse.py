# Diccionario de texto a Morse
MORSE = {
    'A': '.—', 'B': '—...', 'C': '—.—.', 'D': '—..', 'E': '.',
    'F': '..—.', 'G': '——.', 'H': '....', 'I': '..', 'J': '.———',
    'K': '—.—', 'L': '.—..', 'M': '——', 'N': '—.', 'O': '———',
    'P': '.——.', 'Q': '——.—', 'R': '.—.', 'S': '...', 'T': '—',
    'U': '..—', 'V': '...—', 'W': '.——', 'X': '—..—', 'Y': '—.——',
    'Z': '——..',
    '0': '—————', '1': '.————', '2': '..———', '3': '...——',
    '4': '....—', '5': '.....', '6': '—....', '7': '——...', 
    '8': '———..', '9': '————.',
    '.': '.—.—.—', ',': '——..——', '?': '..——..', '"': '.—..—.',
    ' ': ''  # espacio se maneja aparte
}

# Invertimos el diccionario para Morse a texto
MORSE_INV = {v: k for k, v in MORSE.items() if v != ''}

def texto_a_morse(texto):
    resultado = []
    for palabra in texto.upper().split(" "):
        letras = []
        for letra in palabra:
            if letra in MORSE:
                letras.append(MORSE[letra])
        resultado.append(" ".join(letras))
    return "  ".join(resultado)


def morse_a_texto(morse):
    resultado = []
    palabras = morse.split("  ")  # dos espacios separan palabras
    for palabra in palabras:
        letras = palabra.split(" ")
        texto = ""
        for letra in letras:
            if letra in MORSE_INV:
                texto += MORSE_INV[letra]
        resultado.append(texto)
    return " ".join(resultado)


def detectar_y_convertir(entrada):
    # Si solo contiene puntos, rayas y espacios → es Morse
    caracteres_validos = set(".—- ")
    
    if all(c in caracteres_validos for c in entrada):
        # Normalizamos posibles "-" a "—"
        entrada = entrada.replace("-", "—")
        return morse_a_texto(entrada)
    else:
        return texto_a_morse(entrada)


# Programa principal
if __name__ == "__main__":
    texto = input("Ingresa texto o código Morse: ")
    resultado = detectar_y_convertir(texto)
    print("Resultado:", resultado)