'''
    A representtion of the player hand in the game
'''
from random import randint
from Chips import Chips
class Player:
    def __init__(self):
        self.__bankRole = randint(1,5000)
        self.__cardSum=None
        self.bidAmount=None
    
    def placeBid(self):
        while True:
            try:
                self.bidAmount = int(input("How much would you like to bid? $"))
            except:
                print("Please Enter a Valid Number!!!")
                continue
            else:
                if self.bidAmount > self.__bankRole:
                    print(f"You own ${self.__bankRole}, you cant bid ${self.bidAmount}")
                    continue
                break
        return self.bidAmount
    def moneyOwn(self):
        print(f"You own {self.__bankRole} try not to lose it all!")
    def collectWinnings(self):
        self.__bankRole += self.bidAmount
    def giveUpLosts(self):
        self.__bankRole-=self.bidAmount
    
