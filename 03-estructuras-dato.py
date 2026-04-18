# -----------------------------
# 1. LISTA (list)
# -----------------------------
lista = [3, 1, 4, 2]
print("Lista original:", lista)

# Inserción
lista.append(5)
print("Insertar:", lista)

# Actualización
lista[0] = 10
print("Actualizar:", lista)

# Eliminación
lista.remove(4)
print("Eliminar:", lista)

# Ordenación
lista.sort()
print("Ordenada:", lista)


# -----------------------------
# 2. TUPLA (tuple)
# -----------------------------
tupla = (1, 2, 3)
print("\nTupla:", tupla)

# ❌ No se puede modificar directamente (inmutable)
# Para "modificar", se convierte en lista
temp = list(tupla)
temp.append(4)
tupla = tuple(temp)
print("Tupla modificada:", tupla)


# -----------------------------
# 3. CONJUNTO (set)
# -----------------------------
conjunto = {3, 1, 2}
print("\nConjunto:", conjunto)

# Inserción
conjunto.add(5)
print("Insertar:", conjunto)

# Eliminación
conjunto.remove(1)
print("Eliminar:", conjunto)

# No hay actualización directa (se elimina y agrega)
conjunto.add(10)
print("Actualizar (simulado):", conjunto)

# Ordenación (convertir a lista)
print("Ordenado:", sorted(conjunto))


# -----------------------------
# 4. DICCIONARIO (dict)
# -----------------------------
diccionario = {"nombre": "Maicol", "edad": 20}
print("\nDiccionario:", diccionario)

# Inserción
diccionario["ciudad"] = "Bogotá"
print("Insertar:", diccionario)

# Actualización
diccionario["edad"] = 21
print("Actualizar:", diccionario)

# Eliminación
del diccionario["nombre"]
print("Eliminar:", diccionario)

# Ordenación (por claves)
dic_ordenado = dict(sorted(diccionario.items()))
print("Ordenado:", dic_ordenado)