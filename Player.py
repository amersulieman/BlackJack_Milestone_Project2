'''
    A representtion of the player hand in the game
'''
from random import randint
from Chips import Chips
class Player:
    def __init__(self):
        self.hasACE = False
        self.bankRole = randint(1,5000)
        self.cardSum=None
        self.bidAmount=None
    def placeBid(self):
        while True:
            try:
                self.bidAmount = int(input("How much would you like to bid? $"))
            except:
                print("Please Enter a Valid Number!!!")
                continue
            else:
                if self.bidAmount > self.bankRole:
                    print(f"You own ${self.bankRole}, you can't bid ${self.bidAmount}")
                    continue
                break
    def moneyOwn(self):
        print(f"You own ${self.bankRole} try not to lose it all!")
    def collectWinnings(self):
        self.bankRole += self.bidAmount
    def giveUpLosts(self):
        self.bankRole-=self.bidAmount
    
