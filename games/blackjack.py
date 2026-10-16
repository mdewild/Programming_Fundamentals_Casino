from random import shuffle, randint

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Omdat nooit meer of minder dan 52 kaarten in het spel mogen zijn, wordt het deck na elk spel opnieuw geschud.
def deck_fresh():
    deck = [f'{suit}{rank}' for suit in SUITS for rank in RANKS]
    return deck

def deck_shuffle(deck):
    shuffle(deck)
    return deck


def deal(deck):
    hand_player = []
    hand_dealer = []
    for i in range(2):
        hand_player.append(deck.pop(randint(0, len(deck)-1)))
        hand_dealer.append(deck.pop(randint(0, len(deck)-1)))
        #print(len(deck))
    return [hand_player, hand_dealer]

#TODO deze functie is nog niet af
def choose_move():
    print('1. Hit, 2 Stand')
    choice_move = int(input("Wat wilt u doen? "))

#TODO hier moet nog bij dat de waarde van A verandert als >21
def value_hand(hand):
    value_hand_total = 0
    for card in hand:
        print(card)
        value_raw = card.strip('♠♥♦♣')
        print(value_raw)
        if value_raw not in ('A', 'J', 'K', 'Q'):
            value_hand_total += int(value_raw)
        elif value_raw in ('J', 'K', 'Q'):
            value_hand_total += 10
        else:
            value_hand_total += 11
    return value_hand_total


def winstate(hand_player, hand_dealer):
    if sum(hand_player) > 21:
        winner = 'dealer'
    elif sum(hand_dealer) > 21:
        winner = 'player'
    else:
        winner = None



deck = deck_shuffle(deck_fresh())
hand = deal(deck)[0]
print(value_hand(hand))

