'''
    Main script that runs the Blackjack game Contols the whole game
'''
from Player import Player
from GameActions import GameActions
from DeckOfCard import DeckOfCards

THE_PLAYER= 1
THE_COMPUTER=2
pokerCards = DeckOfCards() 
pokerCards.createCards()   #deck sorted
myPlayer = Player()             #player agains the computer
gameControl = GameActions(myPlayer)     #game actions can be taken such as hit and stay
keepPlaying = True
while keepPlaying:
    print("\tYour turn\n********************************")
    gameCards = pokerCards.deck[:]
    myPlayer.moneyOwn()
    myPlayer.placeBid()
    print()
    gameControl.startNewGame(gameCards)
    print("\tYour cards sum =",myPlayer.cardSum)
    print("*"*30)
    #loop for turns Computer and player
    while True:
        #param 1 is for what list to show
        choice = gameControl.userOptions(1)
        if choice ==1:
            card = gameControl.hit(gameCards)
            print("*"*25)
            print("Your New Card ->",card)
            print("Your new Cards sum =",myPlayer.cardSum)
            print("*"*25)
            if gameControl.bust():
                print("*"*25)
                print("YOU LOST...COMPUTER WILL COLLECT YOUR MONEY...")
                print("*"*25)
                myPlayer.giveUpLosts()
                myPlayer.moneyOwn()
                break #exists the take turns loop back to main loop 
            else:
                continue #goes back to ask player for choices
        elif choice == 2:
            print("You"+gameControl.stay())

        print("Compuer Cards sum =",gameControl.computerCardSum)
        #Computer playing here
        while True:
            card=gameControl.hit(gameCards,THE_COMPUTER)
            print("Computer new Card ->",card,"Cards sum =",gameControl.computerCardSum)
            if gameControl.bust(THE_COMPUTER):
                print("*"*25)
                print("YOU WON...You doubled your bid money...")
                print("*"*25)                
                myPlayer.collectWinnings()
                myPlayer.moneyOwn()
                break # breaks out of computer turn loop    
            elif gameControl.computerCardSum<myPlayer.cardSum:
                continue # let computer hit again if its card sum less than player's
            else:
                print("Computer "+gameControl.stay())
                print("*"*25)               
                print("YOU LOST...COMPUTER WILL COLLECT YOUR MONEY...")
                print("*"*25)
                myPlayer.giveUpLosts()
                myPlayer.moneyOwn()
                break #breaks out of taking turns loop
        break

    userchoice = gameControl.userOptions(2)
    if userchoice==1:
        if myPlayer.bankRole>0:
            continue
        print("You Do not have enough money to play again!!!!!!!")
        break
    elif userchoice==2:
        break

