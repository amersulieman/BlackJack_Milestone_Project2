'''
    Class that represnt the game actions to be taken during the game
'''
from random import shuffle
class GameActions:
    __PLAYER=1
    __COMPUTER=2
    def __init__(self,player):
        self.computerCardSum=0
        self.player=player
    def startNewGame(self,cards):
        shuffle(cards)
        self.player.cardSum=0
        #computer takes two cards
        self.hit(cards,self.__COMPUTER)
        print(f"Computer has {self.hit(cards,self.__COMPUTER)} and Card2 is HIDDEN")
        #player takes two cards
        print(f"Player has {self.hit(cards)} and {self.hit(cards)}")
    def hit(self,gameDeck,whoPlaying=__PLAYER):
        newCard = gameDeck.pop()
        if whoPlaying==self.__PLAYER:
            self.player.cardSum+=self.checkCardValue(newCard)
        else:
            self.computerCardSum+=self.checkCardValue(newCard)
        return newCard
    def stay(self):
        return "Decided to stay!"
    def checkCardValue(self,theCard):
        if(theCard.value=="Jack" or theCard.value=="Queen" or theCard.value=="King"):
            return 10
        elif(theCard.value=="Ace"):
            return 1
        #if card withdrawn a normal number
        else:
            return theCard.value
    def bust(self,playing=__PLAYER):
        if playing==self.__PLAYER:
            return self.player.cardSum>21
        else:
            return self.computerCardSum>21