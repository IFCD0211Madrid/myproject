def run(radius) -> float:
    # TODO
    import math
    area = round(math.pi,2) * radius ** 2
    return area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
