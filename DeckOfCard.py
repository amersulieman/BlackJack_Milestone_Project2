'''
    Object representation of a deck of cards
    Uses composition of Card object
'''
from Card import Card
class DeckOfCards:
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    def __init__(self,nums):
        self.numOfCards = nums
        self.deck=list()

    def createCards(self):
        for suit in self.suits:
            ace = Card(suit,"Ace")
            jack = Card(suit,"Jack")
            queen = Card(suit,"Queen")
            king = Card(suit,"King")
            self.deck.append(ace)
            for num in range(2,11):
                newCard=Card(suit,num)
                self.deck.append(newCard)
            self.deck.append(jack)
            self.deck.append(queen)
            self.deck.append(king)
    def __len__(self):
        return self.numOfCards

deck = DeckOfCards(52)
deck.createCards()
