print("Welkom bij roulette!")
print("-"*50)
print("Inzetopties: 1 rood, 2 zwart, 3 even, 4 oneven, 0 stoppen.")

def player_move(amount_available):
    """
    :param amount_available:    hoeveelheid geld beschikbaar om in te zetten
    :return:                    nieuwe hoeveelheid geld beschikbaar
    """

    while True:
        choice_game = int(input("Waarop wilt u inzetten? "))
        if not (choice_game == 0 or choice_game == 1 or choice_game == 2 or choice_game == 3 or choice_game == 4):
            print("Dat is geen geldige keuze.")
            continue
        if choice_game == 0:
            print(f"Bedankt voor het spelen, {name_first.capitalize()}! Hopelijk tot snel.")
            break
        amount_wager = float(input("Hoeveel euro wilt u inzetten? "))
        if amount_wager <= 0 or amount_wager > amount_available:
            print("Dat is geen geldig bedrag.")
            continue
        else:
            amount_available -= amount_wager

#    spin = (number_round * 7) % 37
spin = random.randint(1, 36)
#    number_round += 1
even = True if spin % 2 == 0 else False
if spin <= 18:
    if even:
        colour = "black"
    else:
        colour = "red"
elif even:
    colour = "red"
else:
    colour = "black"

match choice_game:
    case 1: win = True if colour == "red" else False
    case 2: win = True if colour == "black" else False
    case 3: win = True if even else False
    case 4: win = True if not even else False

if win:
    amount_available += 2 * amount_wager
    print(f"\nU heeft € {2 * amount_wager} gewonnen ({spin}", "even" if even else "oneven", f"{colour})!")
    print(f"Uw nieuwe saldo is € {"{:.2f}".format(amount_available)}")
else:
    print(f"\nHelaas heeft u niet gewonnen. Uw nieuwe saldo is € {"{:.2f}".format(amount_available)}")
    if amount_available <= 0:
        exit(2)