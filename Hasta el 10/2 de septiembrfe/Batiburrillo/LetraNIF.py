letras = "TRWAGMYFPDXBNJZSQVHLCKE"

def letra_nif(dni: int) -> str:
    resto = dni % 23
    print(letras[resto:resto+1])
    return letras[resto]


for _ in range(23):
    letra = letra_nif(_) 
    print(letra)
