def run(text):
    # TODO
    num_vowels = 0
    for vocal in text:
        if vocal in ('aeiouAEIOUáéíóúÁÉÍÓÚ'):
            num_vowels += 1
    return num_vowels


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
