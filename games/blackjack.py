from random import shuffle, randint

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Omdat nooit meer of minder dan 52 kaarten in het spel mogen zijn, wordt het deck na elk spel opnieuw geschud.

#Een te hoog bedrag invullen en dan een acceptabel bedrag veroorzaakt een type error in regel 128. Een puzzel voor de liefhebber.
def choose_wager(amount_available):
    choice_wager = float(input(f"\nHoeveel wilt u inzetten (u heeft {amount_available:.2f})? €"))
    if choice_wager <= amount_available:
        return choice_wager
    else:
        print(f"Dat is meer dan u beschikbaar heeft (€{amount_available:.2f})")
        choose_wager(amount_available)

# deck_fresh maakt een nieuw (geordend) deck aan, omdat bij elke ronde een nieuw deck vereist wordt. Een vers pak kaarten.
def deck_fresh():
    deck = [f'{suit}{rank}' for suit in SUITS for rank in RANKS]
    return deck

def deck_shuffle(deck):
    shuffle(deck)
    return deck

#Ivm DRY is het geven van een enkele kaart een aparte functie

def card_draw(deck):
    return deck.pop()

def deal(deck):
    hand_player = []
    hand_dealer = []
    hand_player.extend([card_draw(deck), card_draw(deck)])
    hand_dealer.extend([card_draw(deck), card_draw(deck)])
    return (hand_player, hand_dealer)


def show_hands(hand_dealer, hand_player, hidden_card):
    print(f"\nDealer:", end='')
    for i in range(len(hand_dealer)):
        print(f'|{'??' if hidden_card and i == 1 else hand_dealer[i]}| ', end='')
    print(f"\nSpeler:", end='')
    for i in range(len(hand_player)): print('|' + hand_player[i] + '| ', end='')


def hit(hand_dealer, hand_player, deck):
    hand_player.append(card_draw(deck))
    return winstate(hand_player, hand_dealer)


def stand(hand_dealer, hand_player, deck):
    while value_hand(hand_dealer) < 17:
        hand_dealer.append(card_draw(deck))
    chose_stand = True
    return winstate(hand_player, hand_dealer, chose_stand)


def choose_move(hand_dealer, hand_player, deck, chose_stand = False):
    show_hands(hand_dealer, hand_player, True)
    #chose_stand gaat naar True in chose_stand. Dit voorkomt dat je kaarten kunt trekken na het kiezen van stand.
    if not chose_stand:
        print('\n\n1. Hit, 2. Stand')
        move = int(input("Wat wilt u doen? "))
        if move == 1:
            return hit(hand_dealer, hand_player, deck)
        else:
            return stand(hand_dealer, hand_player, deck)


def value_hand(hand):
    value_hand_total = 0
    count_aces = 0
    for card in hand:
        value_raw = card.strip('♠♥♦♣')
        if value_raw not in ('A', 'J', 'K', 'Q'):
            value_hand_total += int(value_raw)
        elif value_raw in ('J', 'K', 'Q'):
            value_hand_total += 10
        else:
            value_hand_total += 11
            count_aces += 1
    while value_hand_total > 21:
        if count_aces == 0:
            break
        else:
            value_hand_total -= 10
            count_aces -= 1
    return value_hand_total


def winstate(hand_player, hand_dealer, chose_stand = False):
    value_player = value_hand(hand_player)
    value_dealer = value_hand(hand_dealer)

    if value_player > 21:
        winner = 'dealer'
    elif value_dealer > 21:
        winner = 'player'
    elif value_player > value_dealer and value_dealer >= 17:
        winner = 'player'
    elif chose_stand:
        if value_dealer > value_player:
            winner = 'dealer'
        elif value_player > value_dealer:
            winner = 'player'
        else:
            winner = None
    else: winner = None
    return winner


def game_blackjack(amount_available):
    while True:
        print(f'\nWelkom aan de blackjacktafel. U heeft €{amount_available:.2f}')
        print('-'*50)
        print('1. Spelen, 2. Stoppen.')
        if int(input('Wat wilt u doen? ')) == 2:
            return amount_available
        else:
            deck = deck_shuffle(deck_fresh())
            deck_dealt = deal(deck)
            hand_player = deck_dealt[0]
            hand_dealer = deck_dealt[1]
            amount_wager = choose_wager(amount_available)
            amount_available -= amount_wager
            print('\nDe dealer schudt en deelt de kaarten.')
            while True:
                winner = choose_move(hand_dealer, hand_player, deck)
                #show_hands() moet hier steeds apart aangeroepen worden omdat de tweede dealerkaart anders te vroeg wordt onthuld (die aanroep zit in choose_move())
                if winner == 'player':
                    show_hands(hand_dealer, hand_player, False)
                    if value_hand(hand_dealer) > 21:
                        amount_available += 2 * amount_wager
                    else: amount_available += 1.5 * amount_wager
                    print(f'\nU wint! U heeft nu €{amount_available:.2f}.')
                    break
                elif winner == 'dealer':
                    show_hands(hand_dealer, hand_player, False)
                    print(f'\nDealer wint! U heeft nog €{amount_available:.2f}.')
                    break
                elif winner == None:
                    # dit if-statement voorkomt dat gelijkspel wordt uitgeroepen als de speler nog kaarten kan trekken
                    if value_hand(hand_dealer) == value_hand(hand_player):
                        show_hands(hand_dealer, hand_player, False)
                        amount_available += amount_wager
                        print(f'\nGelijkspel. U heeft weer €{amount_available:.2f}.')
                        break


