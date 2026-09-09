# Introducir la frase
frase = input('Introduce una frase: ').lower()

# Alternativa 1
# 2. Inicializar un diccionario para contar las vocales
conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# 3. Contar la aparición de cada vocal
for caracter in frase:
    if caracter in conteo_vocales:
        conteo_vocales[caracter] += 1

# 4. Mostrar los resultados
print("\nFrecuencia de cada vocal:")
for vocal, cantidad in conteo_vocales.items():
    print(f"Vocal '{vocal}': {cantidad}")

# Alternativa 2
# 2. Definir las vocales a buscar
vocales = ['a', 'e', 'i', 'o', 'u']

# 3. Contar e imprimir la frecuencia de cada vocal
print("\nFrecuencia de cada vocal:")
for vocal in vocales:
    cantidad = frase.count(vocal)
    print(f"Vocal '{vocal}': {cantidad}")

# Alternativa 3
# 2. Definir una lambda que cuente cuántas veces aparece un carácter específico
contar_vocal = lambda v: len(list(filter(lambda c: c == v, frase)))

# 3. Aplicar la lambda para cada vocal
print("\nFrecuencia de cada vocal:")
for v in "aeiou":
    print(f"Vocal '{v}': {contar_vocal(v)}")