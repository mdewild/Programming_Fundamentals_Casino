# Verwerkingsopdracht week 3 Martijn de Wild
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

