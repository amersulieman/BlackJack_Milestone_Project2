'''
    Object representation of a deck of cards
    Uses composition of Card object
'''
from Card import Card

class DeckOfCards:
    #cards 4 kinds of suits
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    def __init__(self):
        self.deck=list()

    def createCards(self):
            #For every suit, we have 13 cards : [ACE, 2-10, Jack, Queen, King]
        for suit in self.suits:
            #ace created
            ace = Card(suit,"Ace")
            self.deck.append(ace)
            for num in range(2,11):
                #cards between 2-10 created
                newCard=Card(suit,num)
                self.deck.append(newCard)
            #jack,queen,king are created
            jack = Card(suit,"Jack")
            queen = Card(suit,"Queen")
            king = Card(suit,"King")
            self.deck.append(jack)
            self.deck.append(queen)
            self.deck.append(king)
    def __len__(self):
        return len(self.deck)
        

