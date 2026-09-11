def run(texts: list) -> list:
    # TODO
    nueva_lista = []
    for palabra in texts:
        letras = list(palabra)
        nueva_lista.extend(letras)
    chars = nueva_lista
    return chars


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
