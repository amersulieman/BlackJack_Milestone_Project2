'''
    Class that represnt the game actions to be taken during the game
'''
from Player import Player
from random import shuffle
class GameActions:
    PLAYER=1
    COMPUTER=2
    def __init__(self,player):
        self.computerCardSum=0
        self.player=player
    def startNewGame(self,cards):
        shuffle(cards)
        self.player.cardSum=0
        #computer takes two cards
        self.hit(cards,self.COMPUTER)
        print(f"Computer has {self.hit(cards,True)} and Card2 is Hidden")
        #player takes two cards
        print(f"Player has {self.hit(cards)} and {self.hit(cards)}")
    def hit(self,gameDeck,whoPlaying=PLAYER):
        newCard = gameDeck.pop()
        if whoPlaying==self.PLAYER:
            self.player.cardSum+=self.checkCardValue(newCard)
        else:
            self.computerCardSum+=self.checkCardValue(newCard)
        return newCard
    def stay(self):
        print("Decided to stay!")
    def checkCardValue(self,theCard):
        if(theCard.value=="Jack" or theCard.value=="Queen" or theCard.value=="King"):
            return 10
        
        elif(theCard.value=="Ace"):
            while True:
                try:
                   value = int(input("You withdrawn Ace..\nWould you like to count Ace as 1 or 11: "))
                except :
                    print("CHOOSE APPROPRITAE VALUE!!!!!!")
                    continue
                else: 
                    if value==11 or value ==1:
                        return value
                    continue 
        else:
            return theCard.value
