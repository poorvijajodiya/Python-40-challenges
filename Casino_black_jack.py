import random
import time
class Card:
    def __init__(self,rank,value,suit):
        self.rank = rank
        self.value = int(value)
        self.suit = suit

    def display_card(self):
        print("{} of {}".format(self.rank,self.suit))

class Deck:
    def __init__(self):
        self.cards = []
    def build_deck(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':'10','Q':10,'K':10,'A':11,}
        for suit in suits:
            for rank,value in ranks.items():
                c = Card(rank,value,suit)
                self.cards.append(c)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        a = self.cards.pop()
        return a


class Player:
    def __init__(self):
        self.hand  = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self,deck):
        for i in range(2):
            b  = deck.deal_card()
            self.hand.append(b)

    def display_hand(self):
        print("Player's Hand:")
        for card in self.hand:
            card.display_card()

    def hit(self,deck):
        card = deck.deal_card()
        self.hand.append(card)

    def  get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == 'A':
                ace_in_hand = True
        if self.hand_value>21 and ace_in_hand:
            self.hand_value -= 10
        print("Total value: " + str(self.hand_value))

    def update_hand(self,deck):
        if self.hand_value<21:
            inp = input("Would you like to hit(y/n): ").lower()
            if inp.startswith('y'):
                self.hit(deck)
            else:
                self.playing_hand = False
        else:
            self.playing_hand = False

class Dealer:
    def __init__(self):
        self.hand  = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self,deck):
        for i in range(2):
            b  = deck.deal_card()
            self.hand.append(b)

    def display_hand(self):
        input("Press enter to reveal the dealer's card: ")
        for card in self.hand:
            card.display_card()
            time.sleep(1)


    def hit(self,deck):
        self.get_hand_value()
        while self.hand_value<17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
        print("\nDealer is set with a total of " + str(len(self.hand)) + "cards.")

    def  get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == 'A':
                ace_in_hand = True
        if self.hand_value>21 and ace_in_hand:
            self.hand_value -= 10


class Game:
    def __init__(self,money):
        self.money = int(money)
        self.bet = 20
        self.winner = ""

    def set_bet(self):
        betting = True
        while betting:
            bet = int(input("How much money would you like to bet (min bet is $20): "))
            if bet<20:
                bet = 20
            if bet>self.money:
                print("Sorry you cannot afford the bet")
            else:
                self.bet = bet
                betting = False

    def scoring(self,p_hand_value,d_hand_value):
        if p_hand_value == 21:
            print("got black jack You win")
            self.winner = 'p'
        elif d_hand_value == 21:
            print("dealer got black jack you loose ")
            self.winner = 'd'
        elif p_hand_value > 21:
            print("you went over 21 you loose")
            self.winner = 'd'
        elif d_hand_value > 21:
            print("dealer went over 21 you win")
            self.winner = 'p'
        else:
            if p_hand_value>d_hand_value:
                print("Dealer gets " + str(d_hand_value) + ". You win!")
                self.winner = 'p'
            elif p_hand_value<d_hand_value:
                print("Dealer gets " + str(d_hand_value) + ". You loose!")
                self.winner = 'd'
            else:
                print("Dealer gets " + str(d_hand_value) + ". It is a push!")
                self.winner = 'Tie'

    def payout(self):
        if self.winner == 'p':
            self.money += self.bet
        elif self.winner == 'd':
            self.money -= self.bet

    def display_money(self):
        print("Current Money: ${}".format(self.money))

    def display_money_and_bet(self):
        print("Current Money: ${}\t\t\tcurrent bet: ${}".format(self.money,self.bet))

print("Welcome to the Blackjack App\nThe minimum bet at this table is $20.")
money = int(input("How much money are you willing to play with today: "))
game = Game(money)
active = True
while active:
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()
    player = Player()
    dealer = Dealer()
    game.display_money()
    game.set_bet()
    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)
    game.display_money_and_bet()
    print("The dealer is showing a {} of {}.".format(dealer.hand[0].rank,dealer.hand[0].suit))
    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)
    dealer.hit(game_deck)
    dealer.display_hand()
    game.scoring(player.hand_value,dealer.hand_value)
    game.payout()
    if game.money<20:
        active = False
        print("Sorry, you ran out of money. Please try again.")
