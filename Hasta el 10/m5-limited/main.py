def run(limit: int) -> None:
    # TODO
    #valorDado = float(input('Escribe un número: '))
    valorDado = limit
    multiplo = 1
    while multiplo*5 < valorDado:
        print(multiplo*5)
        multiplo = 3
    print('No hay más múltiplos')

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
