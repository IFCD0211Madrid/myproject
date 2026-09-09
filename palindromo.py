import unicodedata

def palindromo(frase:str) -> bool:
    minusculas: str  = frase.lower()
    limpia: str      = minusculas.replace(' ','')
    # Descompone los caracteres (ej. 'á' -> 'a' + tilde)
    normalizada: str = unicodedata.normalize('NFD', limpia)
    # Codifica a ASCII ignorando los caracteres no pertenecientes (las tildes)
    sin_acentos:str  = normalizada.encode('ascii', 'ignore').decode('utf-8')
    invertida: str  = ''
    for caracter in reversed(sin_acentos):
        invertida += caracter
    print(invertida);
    if sin_acentos==invertida:
        print('Es un palíndromo')
    else:
        print('No es un palíndromo')

palindromo('Dábale arroz a la zorra el abad')
palindromo('Prueba')