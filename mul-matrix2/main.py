def run(A: list, B: list) -> list:
    def multiplicarVectores(X: list, Y: list) -> int:
        return sum(x * y for x, y in zip(X, Y))

    matriz = []
    for i in range(len(A)):
        fila = []
        # Extraemos la columna j de B
        for j in range(len(B[0])):
            columna_B = [fila_B[j] for fila_B in B]
            val = multiplicarVectores(A[i], columna_B)
            fila.append(val)
        matriz.append(fila)

    return matriz


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
