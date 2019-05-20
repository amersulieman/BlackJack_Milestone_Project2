'''
    Main script that runs the Blackjack game Contols the whole game
'''
from Player import Player
from GameActions import GameActions
from DeckOfCard import DeckOfCards

pokerCards = DeckOfCards() 
pokerCards.createCards()                #deck sorted
myPlayer = Player()                     #player against the Dealer
gameControl = GameActions(myPlayer)     #game actions can be taken such as hit and stay
keepPlaying = True
while keepPlaying:
    gameControl.clearScreen()
    gameCards = pokerCards.deck[:]
    myPlayer.moneyOwn()
    myPlayer.placeBid()
    print()
    reached21 = gameControl.startNewGame(gameCards)
    #if reached21 != True, it means the two cards the player has total to 21
    if reached21!=True:
        #loop for turns dealer and player
        gameControl.takeTurns(gameCards)    
    if gameControl.replay():
        continue
    else:
        break
