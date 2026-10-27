# Verwerkingsopdracht week 3 Martijn de Wild
# Exit codes: 1 = gebruiker te jong | 2 = te weinig budget | 3 = gebruiker verlaat casino





import profiles
from games import roulette, slots, blackjack



def update_games_played(player_current, game_played):
    if game_played not in profiles.players[player_current]['games_played']:
        profiles.players[player_current]['games_played'][game_played] = 1
    else:
        profiles.players[player_current]['games_played'][game_played] += 1



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
    print(f"Uw huidige saldo is €{amount_available:.2f}")

def account_change_existing(name_first):
    if name_first in profiles.players:
        global player_current
        player_current = name_first
    else:
        print('Deze speler bestaat nog niet. Check de spelling of maak een nieuw account aan.')



def account_change():
    global player_current
    while True:
        print('\naccount wisselen: 1. bestaand account, 2. nieuw account, 0. annuleren')
        choice_menu = int(input('Wat wilt u doen? '))
        match choice_menu:
            case 0:
                break
            case 1:
                account_change_existing(input('Geef de voornaam van een andere, bestaande account: ').title())
            case 2:
                player_current = profiles.account_make_new(input('Geef de voornaam waarmee u de nieuwe account wilt maken: ').title())
                break


def menu_account():
    while True:
        print('\nAccountmenu: 1. account bekijken, 2. account wisselen, 0. terug')
        choice_menu = int(input('Wat wilt u doen? '))
        match choice_menu:
            case 0: break
            case 1: account_show()
            case 2: account_change()



def account_show():
    print(f"""
    Account van:    {profiles.players[player_current]['preference_address']} {profiles.players[player_current]['name_first']} {profiles.players[player_current]['name_last']}
    Geboortedatum:  {profiles.players[player_current]['date_birth']}""")


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
                    update_amount_available(player_current, slots.game_slots(get_amount_available(player_current)))
                    game_played = 'slots'
                elif menu_games_choice == 2:
                    update_amount_available(player_current, roulette.game_roulette(get_amount_available(player_current)))
                    game_played = 'roulette'
                elif menu_games_choice == 3:
                    update_amount_available(player_current, blackjack.game_blackjack(get_amount_available(player_current)))
                    game_played = 'blackjack'
                elif menu_games_choice == 0:
                    break
                else:
                    print("Dat is geen geldige keuze.")
                    game_played = None
                if game_played != None:
                    update_games_played(player_current, game_played)
        elif menu_main_choice == 2:
            show_saldo(get_amount_available(player_current))
        elif menu_main_choice == 3:
            menu_account()
        elif menu_main_choice == 0:
            print(f"Bedankt voor het spelen, {profiles.players[player_current]['name_first']}, en tot snel!")
            exit(3)
        else:
            print("Dat is geen geldige optie.")




main()