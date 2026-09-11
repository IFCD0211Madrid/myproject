def run(arc_A: float) -> float:
    # TODO
    import math
    PI = round(math.pi,2)
    radio = (arc_A * 2) / PI
    area = round(radio ** 2, 10)
    return area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
