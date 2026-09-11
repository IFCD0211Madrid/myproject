def run(text1: str, text2: str) -> int:
    # TODO
    #Cadenas de distinta longitud
    if len(text1) != len(text2):
        return -1
    #Calculo distancia Hamming
    dhamming = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            dhamming += 1
    return dhamming


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
