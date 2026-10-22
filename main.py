# Verwerkingsopdracht week 3 Martijn de Wild
# Exit codes: 1 = gebruiker te jong | 2 = te weinig budget | 3 = gebruiker verlaat casino

AGE_LEGAL = 18
DATE_YEAR_CURRENT = 2026
SURCHARGE_ENTRY = 1.50
SURCHARGE_ADMIN = 0.63
SURCHARGE_TAX = 3.00
AMOUNT_WAGER_MIN = 1.00

from games import roulette, slots, blackjack


def check_age(date_birth):
    """
    Checks if player is 18 yrs or older
    :param date_birth: date of player birth "dd-mm-yyyy"
    :return: True if older, False if younger
    """
    date_day_birth, date_month_birth, date_year_birth = date_birth.split("-")
    return True if int(DATE_YEAR_CURRENT) - int(date_year_birth) > AGE_LEGAL else False


def determine_salutation():
    """
    Queries name and preferred form of address of player
    :return: fills global variables name_last, name_first and preference_address
    """
    global name_last, name_first, preference_address
    name_last = input("Wat is uw achternaam? ").capitalize()
    name_first = input("Wat is uw voornaam? ").capitalize()
    preference_gender = input("Wat is uw gewenste aanspreekvorm (kies uit m/v/x)? ")
    if preference_gender == "m":
        preference_address = "hr."
    elif preference_gender == "v":
        preference_address = "mevr."
    elif preference_gender == "x":
        preference_address = "mx."
    else:
        preference_address = ""


def amount_available_check(amount_start, surcharge_total):
    return True if (amount_start - surcharge_total) > AMOUNT_WAGER_MIN else False


def show_welcome_message(amount_start, surcharge_total, amount_available):
    print("\nWelkom in het casino. Dit zijn uw gegevens:")
    print("-"*50)
    print(f"""
        {preference_address} {name_last}
        Startbudget:    €{"{:.2f}".format(amount_start)}
        Vaste kosten:   €{"{:.2f}".format(surcharge_total)}
        Speelbudget:    €{"{:.2f}".format(amount_available)}""")


def show_menu_main():
    print("\nHoofdmenu")
    print("-" * 50)
    print("""
        1. Spellen
        2. Saldo
        3. Account
        0. Stop""")
    return int(input("\nMaak uw keuze: "))


def show_menu_games():
    print("\nSpellen")
    print("-" * 50)
    print("""
        1. Fruitmachine
        2. Roulette
        3. Blackjack
        0. Terug""")
    return int(input("\nMaak uw keuze: "))


def show_saldo(amount_available):
    print(f"Uw huidige saldo is €{"{:.2f}".format(amount_available)}")


def show_account(date_birth):
    print(f"""
    Account van:    {preference_address} {name_first} {name_last}
    Geboortedatum:  {date_birth}""")


def main():
    date_birth = input("Om toegelaten te worden moet u 18 jaar of ouder zijn. Wat is uw geboortedatum (dd-mm-yyyy)? ")
    if check_age(date_birth):
        print("welkom in Casino de Gouden Driehoek, waar geld wél gelukkig maakt!")
    else:
        print("Helaas bent u niet oud genoeg om te spelen.")
        exit(1)

    determine_salutation()
    surcharge_total = SURCHARGE_ENTRY + SURCHARGE_ADMIN + SURCHARGE_TAX
    amount_start = int(input(f"Geachte {preference_address} {name_last}, beste {name_first}, wat is uw startbudget in euro? €"))
    if not amount_available_check(amount_start, surcharge_total):
        print("Helaas is dat niet genoeg geld om te spelen.")
        exit(2)
    amount_available = amount_start - surcharge_total
    show_welcome_message(amount_start, surcharge_total, amount_available)

    while True:
        menu_main_choice = show_menu_main()
        if menu_main_choice == 1:
            while True:
                menu_games_choice = show_menu_games()
                if menu_games_choice == 1:
                    amount_available = slots.game_slots(amount_available)
                elif menu_games_choice == 2:
                    amount_available = roulette.game_roulette(amount_available)
                elif menu_games_choice == 3:
                    amount_available = blackjack.game_blackjack(amount_available)
                elif menu_games_choice == 0:
                    break
                else:
                    print("Dat is geen geldige keuze.")
        elif menu_main_choice == 2:
            show_saldo(amount_available)
        elif menu_main_choice == 3:
            show_account(date_birth)
        elif menu_main_choice == 0:
            print(f"Bedankt voor het spelen, {name_first}, en tot snel!")
            exit(3)
        else:
            print("Dat is geen geldige optie.")




main()