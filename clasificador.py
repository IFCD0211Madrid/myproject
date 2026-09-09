def clasificador() -> str:
    nombre = input('Escribe tu nombre: ').upper()
    sexo = input('Indica tu sexo (M,F,O): ').upper()

    return 'A' if ((sexo == 'F' and nombre < 'M') or (sexo == 'M' and nombre > 'N')) else 'B'

print (f'Tu grupo es el \'{clasificador()}\'')