def run(letters: str) -> list[str]:
    # TODO
    mayusculas = []
    minusculas = []
    for letter in letters:
        if letter == ' ':
            mayusculas.clear()
            minusculas.clear()
        elif letter.isupper():
            mayusculas.append(letter)
        elif letter.islower():
            minusculas.append(letter)
    queue = mayusculas + minusculas
    return queue


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
