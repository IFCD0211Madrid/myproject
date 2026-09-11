def run(player1: str, player2: str) -> int:
    # TODO
    jugador1 = player1.upper()
    jugador2 = player2.upper()
    if jugador1 == jugador2:
        return 0
    elif (jugador1 == "ROCK" and jugador2 == "SCISSORS") \
        or (jugador1 == "PAPER" and jugador2 == "ROCK")  \
        or (jugador1 == "SCISSORS" and jugador2 == "PAPER"):
        return 1
    else:
        return 2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
