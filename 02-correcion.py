def imprimir_cadenas(cadena1, cadena2):
    contador_numeros = 0

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1 + cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(i)
            contador_numeros += 1

    return contador_numeros


# Ejemplo de uso
resultado = imprimir_cadenas("Fizz", "Buzz")
print("Cantidad de números impresos:", resultado)