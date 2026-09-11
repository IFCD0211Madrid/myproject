def run(n: int) -> bool:
    # TODO
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    return is_prime


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
