def run(x: float) -> float:
    # TODO
    # Solución autómáticamente propuesta
    # sin = x - (x ** 3) / 6 + (x ** 5) / 120 - (x ** 7) / 5040
    resto = 180 - x
    numerador = 4 * x * resto
    denominador = 40_500 - x * resto
    sin = numerador / denominador 
    print(f"sin({x}) = {sin}")  
    return sin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
