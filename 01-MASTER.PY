def numeros():
    while True:
        try:
            n1 = int(input("Ingresa el número: "))
            
            if n1 % 2 == 0:
                print("Es par:", n1)
            else:
                print("Es impar:", n1)

        except ValueError:
            print("Error: debes ingresar un número válido")

numeros()
    
    