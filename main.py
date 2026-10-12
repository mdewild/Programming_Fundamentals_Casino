# Verwerkingsopdracht week 1 en 2

# Door Martijn de Wild
# Exit codes: 1 = gebruiker te jong | 2 = te weinig budget

import random

surcharge_entry = 1.50
surcharge_admin = 0.63
surcharge_tax = 3.00
age_min = 18
date_year_current = 2026

print("\nWelkom bij Casino De Gouden Driehoek, waar geld niet gelukkig maakt.\nLaten we beginnen met het aanmaken van een gebruikersaccount.")
name_last = input("Wat is uw achternaam? ")
name_first = input("Wat is uw voornaam? ")
preference_gender = input("Wat is uw gewenste aanspreekvorm (m/v/x)? ")
if preference_gender == "m":
    preference_address = "hr."
elif preference_gender == "v":
    preference_address = "mevr."
elif preference_gender == "x":
    preference_address = "mx."
else: preference_address = ""

# TODO hoofdletters bij voorvoegsels corrigeren
print(f"\nGeachte {preference_address} {name_last.title()}, beste {name_first.capitalize()}, welkom in het casino!\nVoordat we verder gaan, hebben we nog wat meer informatie nodig.")

# TODO invoerdomeinen beperken, rekenen met maanden en jaren
date_birth = input("Wat is uw geboortedatum (dd-mm-yyyy)? ")
date_day_birth, date_month_birth, date_year_birth = date_birth.split("-")
if int(date_year_current) - int(date_year_birth) < 18:
    print("Leuk geprobeerd broekie!")
    exit(1)

amount_player_start = float(input("Wat is uw startbudget in €? "))
print("\nUw gegevens samengevat")
print("-"*50)
print(f"Naam:\t\t\t\t\t\t{preference_address} {name_first.capitalize()} {name_last.title()}")
print(f"Geboortedatum:\t\t\t\t{date_birth}")
print(f"Startbudget:\t\t\t\t€ {"{:.2f}".format(amount_player_start)}")
print(f"Vaste kosten per sessie:\t€ {"{:.2f}".format(surcharge_entry + surcharge_admin + surcharge_tax)}")
amount_available = amount_player_start - surcharge_entry - surcharge_admin - surcharge_tax
print(f"Speelsaldo:\t\t\t\t\t€ {"{:.2f}".format(amount_available)}")
print("\nSpeelsaldo is", "voldoende" if amount_available >= 10.0 else "onvoldoende", "voor toegang")
if amount_available < 0:
    exit(2)

print("Welkom bij roulette!")
print("-"*50)
print("Inzetopties: 1 rood, 2 zwart, 3 even, 4 oneven, 0 stoppen.")

choice_game = 1
number_round = 1
while choice_game != 0:
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