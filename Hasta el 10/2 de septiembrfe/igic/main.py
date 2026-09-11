def run(price_with_igic: float, igic: float) -> float:
    # TODO
    clean_price = round( price_with_igic / (1 + igic / 100), 2 )
    return clean_price


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
