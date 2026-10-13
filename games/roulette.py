import random

#FIXME tijdelijke variabelen
amount_available = 50.0
name_first = "Jim"


def choose_move():
    """
    Geeft de speler een keuze waarop in te zetten
    :return:        keuze voor inzet (indien geldig)
    """
    while True:
        print("""\n
        Inzetopties:
            1. Rood
            2. Zwart
            3. Even
            4. Oneven
            0. Terug.""")
        choice_move = int(input("\nWaarop wilt u inzetten? "))
        if choice_move in (0, 1, 2, 3, 4):
            return choice_move
        else:
            print("Dat is geen geldige keuze.")


def choose_wager(amount_available):
    choice_wager = float(input("\nHoeveel wilt u inzetten? €"))
    if choice_wager <= amount_available:
        return choice_wager
    else:
        print(f"Dat is meer dan u beschikbaar heeft (€{amount_available})")
        choose_wager(amount_available)


def determine_win(choice_move, amount_wager):
    pass


def game_roulette(amount_available):
    print("\nWelkom bij roulette!")
    print("-" * 50)
    while True:
        choice_move = choose_move()
        amount_wager = choose_wager(amount_available)
        determine_win(choice_move, amount_available)







if not (choose_move == 0 or choose_move == 1 or choose_move == 2 or choose_move == 3 or choose_move == 4):
    print("Dat is geen geldige keuze.")
    continue
if choose_move == 0:
    print(f"Bedankt voor het spelen, {name_first.capitalize()}! Hopelijk tot snel.")
    break
amount_wager = float(input("Hoeveel euro wilt u inzetten? "))
if amount_wager <= 0 or amount_wager > amount_available:
    print("Dat is geen geldig bedrag.")
    continue
else:
    return amount_available - amount_wager
    break

# #    spin = (number_round * 7) % 37
# spin = random.randint(1, 36)
# #    number_round += 1
# even = True if spin % 2 == 0 else False
# if spin <= 18:
#     if even:
#         colour = "black"
#     else:
#         colour = "red"
# elif even:
#     colour = "red"
# else:
#     colour = "black"
#
# match choice_game:
#     case 1: win = True if colour == "red" else False
#     case 2: win = True if colour == "black" else False
#     case 3: win = True if even else False
#     case 4: win = True if not even else False
#
# if win:
#     amount_available += 2 * amount_wager
#     print(f"\nU heeft € {2 * amount_wager} gewonnen ({spin}", "even" if even else "oneven", f"{colour})!")
#     print(f"Uw nieuwe saldo is € {"{:.2f}".format(amount_available)}")
# else:
#     print(f"\nHelaas heeft u niet gewonnen. Uw nieuwe saldo is € {"{:.2f}".format(amount_available)}")
#     if amount_available <= 0:
#         exit(2)