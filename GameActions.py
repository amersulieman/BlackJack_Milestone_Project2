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
        print("\tComputer Cards:")
        print(f"Card 1 ->{self.hit(cards,self.__COMPUTER)}, Card 2 -> HIDDEN")
        #player takes two cards
        print("\tYour Cards:")
        print(f"Card 1 ->{self.hit(cards)}, Card 2 ->{self.hit(cards)}")
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
    def userOptions(self,listOfOptions):
    #validate input
        while True:
            try:   
                if listOfOptions ==1:
                    choice = int(input("Choose one of the options:\n1.HIT\n2.Stay\nchoice = "))
                else:
                    choice = int(input("Play again?\n1.YES\n2.NO\nchoice = "))   
            except ValueError:
                print("Please enter a number -> 1 or 2")
                continue
            else:
                if choice==1 or choice ==2:
                    break
                print("please choose one of the choices on list...")
                continue
        return choice