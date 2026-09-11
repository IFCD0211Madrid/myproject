def run(target_number: int) -> None:
    # TODO
    intentos = 1
    numero = None

    while True:
        numero = int(input('Introduzca número: '))
        if numero == target_number:
            print(f'Enhorabuena has encontrado el número en {intentos} intentos')
            break
        elif numero < target_number:
            print('Mayor')
        elif numero > target_number:
            print('Menor')
        intentos += 1

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
