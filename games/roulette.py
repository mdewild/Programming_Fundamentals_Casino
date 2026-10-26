import random

def choose_move():
    """
    Geeft de speler een keuze waarop in te zetten
    :return:        keuze voor inzet (indien geldig)
    """
    while True:
        print("""
            Inzetopties:
            1. Rood
            2. Zwart
            3. Even
            4. Oneven
            0. Terug""")
        choice_move = int(input("\nWaarop wilt u inzetten? "))
        if choice_move in (0, 1, 2, 3, 4):
            return choice_move
        else:
            print("Dat is geen geldige keuze.")


def choose_wager(amount_available):
    choice_wager = float(input(f"\nHoeveel wilt u inzetten (u heeft {"{:.2f}".format(amount_available)})? €"))
    if choice_wager <= amount_available:
        return choice_wager
    else:
        print(f"Dat is meer dan u beschikbaar heeft (€{"{:.2f}".format(amount_available)})")
        choose_wager(amount_available)


def spin():
    return random.randint(1, 36)


def determine_win(choice_move):
    spin_result = spin()
    even = True if spin_result % 2 == 0 else False
    if spin_result <= 18:
        colour = "zwart" if even else "rood"
    elif even:
        colour = "rood"
    else:
        colour = "zwart"

    print(f"\nRien ne va plus! Het resultaat is: {spin_result}, {colour},", "even." if even else "oneven.")

    match choice_move:
        case 1:
            win = True if colour == "rood" else False
        case 2:
            win = True if colour == "zwart" else False
        case 3:
            win = True if even else False
        case 4:
            win = True if not even else False

    return win


def game_roulette(amount_available):
    print("\nWelkom bij roulette!")
    print("-" * 50)
    while True:
        choice_move = choose_move()
        if choice_move == 0:
            return(amount_available)
        amount_wager = choose_wager(amount_available)
        amount_available -= amount_wager
        if determine_win(choice_move):
            amount_available += 2 * amount_wager
            print(f"Gefeliciteerd! Je hebt €{"{:.2f}".format(2*amount_wager)} gewonnen. Je hebt nu €{"{:.2f}".format(amount_available)}.")
        else:
            print(f"Helaas! Je hebt nog €{"{:.2f}".format(amount_available)}")
            if amount_available <= 0:
                exit(2)