'''
    A representtion of the player in the game
'''
from random import randint
class Player:
    def __init__(self):
        self.bankRole = 500
        self.cardSum=None
    
    def placeBet(self):
        betAmount = randint(1,self.bankRole+1)
        return betAmount
