'''
    A class to represnt poker chips with their colors and values
    Also to handle conversion of money to poker chips
'''
class Chips:
    __gameChips={1000:"YELLOW",500:"PURPLE", 100:"BLACK",50:"ORANGE",25:"GREEN",5:"RED",1:"WHITE"}
    def __init__(self):
        #list of tuples for holding each chipColor and how many of it for the bid
        self.chipsForBid=list()
    def calcChips(self,bidAmount):
        #calculate how many chip of each color to give for the bid amount
        for value in self.__gameChips:
            if bidAmount>value:
                chipColor=self.__gameChips[value]
                numChips = int(bidAmount/value)
                self.chipsForBid.append((numChips,chipColor))
                bidAmount-=(numChips*value)
    def resetBidChips(self):
        self.chipsForBid.clear()
    def __str__(self):
        representation = ""
        for a,b in self.chipsForBid:
            representation+=str(a).center(20)
        representation+="\n"
        for a,b in self.chipsForBid:
            representation+=b.center(20)
        return representation
