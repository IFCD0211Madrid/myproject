def run(fullname: str) -> str:
    # TODO
    nombre_completo =  []
    nombre = fullname.split(',')[1].strip()
    apellidos = fullname.split(',')[0].split()
    nombre_completo.append(nombre)
    #nombre_completo.append(apellidos[0])
    #if len(apellidos) > 1:
    #    nombre_completo.append(apellidos[1])
    for apellido in apellidos:
        nombre_completo.append(apellido)
    #
    iniciales=[cadena[0] for cadena in nombre_completo]
    initials = '.'.join(iniciales).upper() + '.'
    return initials


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
