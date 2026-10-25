# Verwerkingsopdracht week 3 Martijn de Wild
# Exit codes: 1 = gebruiker te jong | 2 = te weinig budget | 3 = gebruiker verlaat casino





import profiles
from games import roulette, slots, blackjack


def get_amount_available(player_current):
    return profiles.players[player_current]['amount_available']

def update_amount_available(player_current, amount_available):
    profiles.players[player_current]['amount_available'] = amount_available



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


def show_account():
    print(f"""
    Account van:    {profiles.players[player_current]['preference_address']} {profiles.players[player_current]['name_first']} {profiles.players[player_current]['name_last']}
    Geboortedatum:  {profiles.players[player_current]['date_birth']}""")

#TODO: amount available moet nog naar profile worden geschreven!
def main():
    global player_current
    player_current = profiles.login()
    # print(profiles.players[player_current])
    while True:
        menu_main_choice = show_menu_main()
        if menu_main_choice == 1:
            while True:
                menu_games_choice = show_menu_games()
                if menu_games_choice == 1:
                    amount_available = slots.game_slots(profiles.players[player_current]['amount_available'])
                elif menu_games_choice == 2:
                    amount_available = roulette.game_roulette(profiles.players[player_current]['amount_available'])
                elif menu_games_choice == 3:
                    amount_available = blackjack.game_blackjack(profiles.players[player_current]['amount_available'])
                elif menu_games_choice == 0:
                    break
                else:
                    print("Dat is geen geldige keuze.")
        elif menu_main_choice == 2:
            show_saldo(profiles.players[player_current]['amount_available'])
        elif menu_main_choice == 3:
            show_account()
        elif menu_main_choice == 0:
            print(f"Bedankt voor het spelen, {profiles.players[player_current]['name_first']}, en tot snel!")
            exit(3)
        else:
            print("Dat is geen geldige optie.")




main()