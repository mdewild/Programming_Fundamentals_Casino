import random


def choose_move():
    """
    Geeft de speler een keuze waarop in te zetten
    :return:        keuze voor inzet (indien geldig)
    """
    while True:
        print("""
            Opties:
            1. Spelen
            0. Terug""")
        choice_move = int(input("\nWat wilt u doen? "))
        if choice_move in (0, 1):
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
    return random.randint(1, 3)


def display_result(spin_result):
    print("\nResultaat: | ", end = "")
    for i in (0, 1, 2):
        if spin_result[i] == 1:
            spin_picture = "DWERG"
        elif spin_result[i] == 2:
            spin_picture = "ELF"
        else:
            spin_picture = "TOVENAAR"
        print(spin_picture, end= " | ")


# Twee linker of twee rechter gelijk: 2x inzet (dit is net anders dan de opdracht...)
# Drie gelijk: 8x inzet
def determine_win():
    spin_result = (spin(), spin(), spin())
    display_result(spin_result)
    if (spin_result[0] == spin_result[1]) ^ (spin_result[1] == spin_result[2]): # ^is XOR
        factor_win = 2
    elif (spin_result[0] == spin_result[1]) and (spin_result[1] == spin_result[2]):
        factor_win = 8
    else:
        factor_win = 0
    return factor_win


def game_slots(amount_available):
    print("\nWelkom bij de fruitmachine!")
    print("-" * 50)
    while True:
        choice_move = choose_move()
        if choice_move == 0:
            return(amount_available)
        amount_wager = choose_wager(amount_available)
        amount_available -= amount_wager
        factor_win = determine_win()
        amount_available += factor_win * amount_wager
        print("\nU wint", (f"€ {"{:.2f}".format(factor_win * amount_wager)}.") if factor_win != 0 else "niets.")
        print(f"U heeft nog €{"{:.2f}".format(amount_available)}")
        if amount_available <= 0:
            exit(2)