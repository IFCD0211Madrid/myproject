def run(u: list, v: list) -> float | None:
    # TODO
    dprod:float = 0
    if len(u) != len(v):
        return None
    for ui, vi in zip(u,v):
        dprod += ui * vi
    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
