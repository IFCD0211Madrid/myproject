def calcular_letra_nie(nie_numeros):
    """
    Calcula la letra del NIE a partir de los 8 dígitos.
    
    Args:
        nie_numeros: String o int con los 8 números del NIE
    
    Returns:
        str: La letra correspondiente
    """
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    # Convertir a string y extraer solo los dígitos
    nie_str = str(nie_numeros).strip()
    
    # Si comienza con X, Y o Z (extranjeros), convertir a número
    if nie_str[0] in 'XYZ':
        nie_str = nie_str.replace('X', '0').replace('Y', '1').replace('Z', '2')
    
    # Obtener los 8 dígitos
    numeros = int(nie_str[:8])
    
    # Calcular módulo 23
    resto = numeros % 23
    
    # Obtener la letra
    letra = letras[resto]
    
    return letra


if __name__ == "__main__":
    # Ejemplo de uso
    nie = "X12345678Q"
    letra = calcular_letra_nie(nie)
    print(f"NIE: {nie}{letra}")
