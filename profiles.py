AGE_LEGAL = 18
DATE_YEAR_CURRENT = 2026
SURCHARGE_ENTRY = 1.50
SURCHARGE_ADMIN = 0.63
SURCHARGE_TAX = 3.00
SURCHARGE_TOTAL = SURCHARGE_ENTRY + SURCHARGE_ADMIN + SURCHARGE_TAX
AMOUNT_WAGER_MIN = 1.00

global players, player_current




def show_welcome_message(amount_start, surcharge_total, amount_available):
    print("\nWelkom in het casino. Dit zijn uw gegevens:")
    print("-"*50)
    print(f"""
        {preference_address} {name_last}
        Startbudget:    €{amount_start:.2f}
        Vaste kosten:   €{SURCHARGE_TOTAL:.2f}
        Speelbudget:    €{amount_available:.2f}""")



def amount_available_check(amount_start, surcharge_total):
    return True if (amount_start - SURCHARGE_TOTAL) > AMOUNT_WAGER_MIN else False


def determine_salutation():
    global name_last, preference_gender, preference_address
    name_last = input("Wat is uw achternaam? ").capitalize()
    preference_gender = input("Wat is uw gewenste aanspreekvorm (kies uit m/v/x)? ")
    if preference_gender == "m":
        preference_address = "hr."
    elif preference_gender == "v":
        preference_address = "mevr."
    elif preference_gender == "x":
        preference_address = "mx."
    else:
        preference_address = ""


def check_age(date_birth):
    date_day_birth, date_month_birth, date_year_birth = date_birth.split("-")
    return True if int(DATE_YEAR_CURRENT) - int(date_year_birth) > AGE_LEGAL else False


def login():
    name_first = input('Log in met uw voornaam: ').title()
    player_current = name_first
    if name_first in players:
        print(f'Welkom terug, {name_first}. Je huidige saldo is €{players[player_current]['amount_available']:.2f}')
        return player_current
    else:
        date_birth = input("Om toegelaten te worden moet u 18 jaar of ouder zijn. Wat is uw geboortedatum (dd-mm-yyyy)? ")
        if check_age(date_birth):
            print("welkom in Casino de Gouden Driehoek, waar geld wél gelukkig maakt!")
        else:
            print("Helaas bent u niet oud genoeg om te spelen.")
            exit(1)
        determine_salutation()
        players[name_first] = {'name_last': name_last, 'name_first': name_first, 'date_birth': date_birth, 'preference_gender': preference_gender, 'preference_address' : preference_address, 'games_played': {}}
        amount_start = int(input(f"Geachte {players[player_current]['preference_address']} {players[player_current]['name_last']}, beste {players[player_current]['name_first']}, wat is uw startbudget in euro? €"))
        if not amount_available_check(amount_start, SURCHARGE_TOTAL):
            print("Helaas is dat niet genoeg geld om te spelen.")
            exit(2)
        amount_available = amount_start - SURCHARGE_TOTAL
        players[name_first]['amount_available'] = amount_available
        show_welcome_message(amount_start, SURCHARGE_TOTAL, amount_available)
        return player_current




#players: {name_first : [name_last, name_first, date_birth, preference_gender, preference_address, amount_available, [games_played]]}
players = {'Jim' : {'name_last' : 'Kirk', 'name_first' : 'Jim', 'date_birth' : '23-12-1995', 'preference_gender' : 'm', 'preference_address' : 'hr.', 'amount_available' : 17.01, 'games_played' : {'blackjack' : 5}},
'Adira' : {'name_last' : 'Tal', 'name_first' : 'Adira', 'date_birth' : '19-06-2003', 'preference_gender' : 'x', 'preference_address' : 'mx.', 'amount_available' : 10.31, 'games_played' : {'roulette' : 3, 'slots' : 5}},
'Jadzia' : {'name_last' : 'Dax', 'name_first' : 'Jadzia', 'date_birth' : '05-11-1999', 'preference_gender' : 'v', 'preference_address' : 'mevr.', 'amount_available' : 742.05, 'games_played' : {'slots' : 31}}
            }
player_current = ''

# login()