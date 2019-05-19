'''
    Class that represnt the game actions to be taken during the game
'''
from random import shuffle
from os import system,name

class GameActions:
    __PLAYER=1
    __COMPUTER=2
    def __init__(self,player):
        self.compHASACE =False
        self.computerCardSum=0
        self.player=player
    def startNewGame(self,cards):
        shuffle(cards)
        self.player.cardSum=0
        self.player.hasACE=False
        self.computerCardSum=0
        self.compHASACE=False
        #computer takes two cards
        compHiddenCard=self.hit(cards,self.__COMPUTER)
        print(compHiddenCard)
        print("\tComputer Cards:")
        print(f"Card 1 ->{self.hit(cards,self.__COMPUTER)}, Card 2 -> HIDDEN")
        #player takes two cards
        print("\n\tYour Cards:")
        print(f"Card 1 ->{self.hit(cards,self.__PLAYER)}, Card 2 ->{self.hit(cards,self.__PLAYER)}")
        print("\tCards sum =",self.player.cardSum)
        print("*"*30)

        #IF first two cards for player == 21 it measn blackjack or tie, no need to proceed
        if self.player.cardSum==21:
            if self.computerCardSum!=21:
                print("BLACKJACK... YOU WON IMMEDIATELY!!! ")
                self.player.collectWinnings()
                return True
            else:
                print("IT IS A TIE.. dealer  has 21 as well! ")
                return True

    def hit(self,gameDeck,whoPlaying):
        newCard = gameDeck.pop()
        if whoPlaying==self.__PLAYER:
            self.player.cardSum+=self.checkCardValue(newCard,self.__PLAYER)
            self.checkForAceTrouble(self.__PLAYER)
        else:
            self.computerCardSum+=self.checkCardValue(newCard,self.__COMPUTER)
            self.checkForAceTrouble(self.__COMPUTER)
        return newCard
    def stay(self):
        return " Decided to stay!"
    def checkCardValue(self,theCard,playing):
        if(theCard.value=="Jack" or theCard.value=="Queen" or theCard.value=="King"):
            return 10
        elif(theCard.value=="Ace"):
            #player
            if playing == self.__PLAYER:
                if self.player.cardSum>10:
                    return 1
                else:
                    self.player.hasACE=True
                    return 11
            #dealer
            elif playing == self.__COMPUTER:
                if self.computerCardSum > 10:
                    return 1
                else:
                    self.compHASACE=True
                    return 11
        #if card withdrawn is a normal number
        else:
            return theCard.value
    def bust(self,playing=__PLAYER):
        if playing==self.__PLAYER:
            return self.player.cardSum>21
        else:
            return self.computerCardSum>21
    def checkForAceTrouble(self,playing):
        if playing == self.__PLAYER:
            if self.player.hasACE == True and self.player.cardSum>21:
                self.player.cardSum-=10
                self.player.hasACE =False
        else:
            if self.compHASACE==True and self.computerCardSum>21:
                self.computerCardSum-=10
                self.compHASACE==False
    def userOptions(self,listOfOptions):
        #validate input
        while True:
            try:   
                if listOfOptions ==1:
                    choice = int(input("Choose one of the options:\n1.HIT\n2.Stay\nchoice = "))
                    print()
                else:
                    choice = int(input("Play again?\n1.YES\n2.NO\nchoice = "))   
                    print()
            except ValueError:
                print("Please enter a number -> 1 or 2")
                continue
            else:
                if choice==1 or choice ==2:
                    break
                print("please choose one of the choices on list...")
                continue
        return choice
    def playerTurn(self,gameCards):
        #param 1 is for what list to show
        choice = self.userOptions(1)
        if choice ==1:
            card = self.hit(gameCards,self.__PLAYER)
            print("...You hit",card)
            print("...Cards sum =",self.player.cardSum)
            print()
            if self.bust():
                print("*"*35)
                print("YOU LOST...dealer WILL COLLECT YOUR MONEY...")
                print("*"*35)
                self.player.giveUpLosts()
                self.player.moneyOwn()
                return False#player bust so they lost
            else:
                return True #Player didn't bust so continue play
        elif choice == 2:
            print("You"+self.stay())
    def dealerTurn(self,gameCards):
        #dealer playing here
        while self.computerCardSum<17 and self.computerCardSum <= self.player.cardSum:
            card=self.hit(gameCards,self.__COMPUTER)
            print(".....Dealer Hit",card,"\n.....Cards sum =",self.computerCardSum)
            if self.bust(self.__COMPUTER):
                print("*"*25)
                print("YOU WON...You doubled your bid money...")
                print("*"*25)                
                self.player.collectWinnings()
                self.player.moneyOwn()
                break   
        else:
            print(".....Dealer"+self.stay())
            if self.computerCardSum == self.player.cardSum:            
                print("IT IS A TIE..")
            elif self.computerCardSum>self.player.cardSum:
                print("*"*25)               
                print("YOU LOST...Dealer WILL COLLECT YOUR MONEY...")
                print("*"*25)
                self.player.giveUpLosts()
            elif self.computerCardSum < self.player.cardSum:
                print("*"*25)
                print("YOU WON...You doubled your bid money...")
                print("*"*25)                
                self.player.collectWinnings()
            self.player.moneyOwn()
    def takeTurns(self,gameCards):
        while True:
            resultPlayer = self.playerTurn(gameCards)
            if resultPlayer == False:
                return
            elif resultPlayer == True:
                continue
            else:
                print("\tDealer Turn")
                print("*"*30)
                print("\tCard sum =",self.computerCardSum)
                self.dealerTurn(gameCards)
                return
    def replay(self):
        userchoice = self.userOptions(2)
        if userchoice==1:
            if self.player.bankRole>0:
                return True
            else:
                print("You Do not have enough money to play again!!!!!!!")
                return False
        elif userchoice==2:
            return False
    def clearScreen(self):
        if name == "nt":
            _ = system('cls')
        else:
            _ = system('clear')