# -----------------------------
# VARIABLE GLOBAL
# -----------------------------
mensaje_global = "Soy una variable global"

# -----------------------------
# 1. FUNCIÓN SIN PARÁMETROS NI RETORNO
# -----------------------------
def saludar():
    print("Hola, esta es una función sin parámetros ni retorno")

# -----------------------------
# 2. FUNCIÓN CON UN PARÁMETRO
# -----------------------------
def saludar_nombre(nombre):
    print("Hola,", nombre)

# -----------------------------
# 3. FUNCIÓN CON VARIOS PARÁMETROS
# -----------------------------
def sumar(a, b):
    print("La suma es:", a + b)

# -----------------------------
# 4. FUNCIÓN CON RETORNO
# -----------------------------
def multiplicar(a, b):
    return a * b

# -----------------------------
# 5. FUNCIÓN DENTRO DE OTRA FUNCIÓN
# -----------------------------
def funcion_externa():
    print("Estoy en la función externa")

    def funcion_interna():
        print("Estoy en la función interna")

    funcion_interna()

# -----------------------------
# 6. USO DE FUNCIONES DEL LENGUAJE
# -----------------------------
def usar_funciones_nativas():
    lista = [1, 2, 3, 4, 5]
    print("Longitud de la lista:", len(lista))  # función nativa
    print("Máximo:", max(lista))               # función nativa
    print("Mínimo:", min(lista))               # función nativa

# -----------------------------
# 7. VARIABLE LOCAL VS GLOBAL
# -----------------------------
def variables():
    mensaje_local = "Soy una variable local"
    print(mensaje_local)   # local
    print(mensaje_global)  # global

# -----------------------------
# EJECUCIÓN DE TODAS LAS FUNCIONES
# -----------------------------
saludar()

saludar_nombre("Maicol")

sumar(5, 3)

resultado = multiplicar(4, 2)
print("Resultado de multiplicar:", resultado)

funcion_externa()

usar_funciones_nativas()

variables()