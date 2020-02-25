import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    
    def __init__(self):
        self.deck = []
        self.create()

    def create(self):
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))
    
    def __str__(self):
        deck_start = ''
        for x in self.deck:
            deck_start += '\n' +x.__str__()
        return 'The deck has:' + deck_start
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single = self.deck.pop()
        return single
    
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def hit(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
    
    def win(self):
        self.total += self.bet
    
    def lose(self):
        self.total -= self.bet
        
def bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Bets must be integers!')
        else:
            if chips.total < chips.bet:
                print('You are unable to place a bet larger than',chips.total)
            else:
                break
            
def hit(deck, hand):
    
    hand.hit(deck.deal())
    hand.adjust()
    
def choice(deck, hand):
    global playing
    
    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's': ")
        
        if x.lower() == 'h':
            hit(deck, hand)
        
        elif x.lower() == 's':
            print("Player stands -- Dealer's turn")
            playing = False
        
        else:
            print('Please try again!')
            continue
        break
    

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def player_busts(player,chips):
    print('Player has busted!')
    chips.lose()

def player_wins(player,dealer,chips):
    print('Player has won!')
    chips.win()

def dealer_busts(player,dealer,chips):
    print('Dealer has lost!')
    chips.win()
    
def dealer_wins(player,dealer,chips):
    print('Dealer has won!')
    chips.lose()
    
def push(player,dealer):
     print("Tie, it's a push!")
     
while True:
    print('Welcome to Blackjack -- Dealer will stand once reaching 17+.')
    
    play_deck = Deck()
    play_deck.shuffle()

    player_hand = Hand()
    player_hand.hit(play_deck.deal())
    player_hand.hit(play_deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.hit(play_deck.deal())
    dealer_hand.hit(play_deck.deal())
    
    player_chips = Chips()
    
    bet(player_chips)
    
    show_some(player_hand, dealer_hand)
    
    while playing:
        choice(play_deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand, player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(play_deck, dealer_hand)
            
        show_all(player_hand, dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand.value,dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(dealer_hand, player_hand)
            
    print("\nPlayer's winnings stand at",player_chips.total)
    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game.lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break