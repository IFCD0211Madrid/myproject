def run(input_date: str, base_year: int) -> str:
    # TODO
    mes_dia_anho = input_date.split('/')
    dia  = f'{mes_dia_anho[1]:>02}'
    mes  = f'{mes_dia_anho[0]:>02}'
    anho = f'{int(mes_dia_anho[2])+base_year!s:>04}'
    output_date = '-'.join([dia,mes,anho])
    return output_date


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
