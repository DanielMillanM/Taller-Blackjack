class Card:
    def __init__(self,symbol,suit):
        self.cost=symbol
        self.symbol = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][symbol-1]
        self.suit = '♥♦♣♠'[suit]

    def show(self):
        print('┌───────┐')
        print(f'| {self.symbol:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.symbol:>2} |')
        print('└───────┘') 

    def score(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost
import random
class Dealer:
    def __init__(self):
        self.deck = []

    def generate(self):
        for i in range(1, 14):
            for j in range(4):
                self.deck.append(Card(i, j))
    
    def Randomize(self, iteration):
        deck = []
        for i in range(iteration):
            card = random.choice(self.deck)
            self.deck.remove(card)
            deck.append(card)
        return deck

    def count(self):
        return len(self.deck)