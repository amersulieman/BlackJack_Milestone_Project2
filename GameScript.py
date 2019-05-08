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
    gameCards = pokerCards.deck[:]
    print("There are",len(gameCards),"Cards")
    myPlayer.moneyOwn()
    myPlayer.placeBid()
    print("You chose to bid $",myPlayer.bidAmount)
    print()
    gameControl.startNewGame(gameCards)
    print("Your cards sum =",myPlayer.cardSum)
    #loop for turns Computer and player
    while True:
        #validate input
        while True:
            try:    
                choice = int(input("Choose one of the options:\n1.HIT\n2.Stay\nYour number of choice = "))
            except:
                print("Please Choose an Approrpiate choice...")
                continue
            else:
                if choice==1 or choice ==2:
                    break
                print("Please Choose an Approrpiate choice...")
                continue
        if choice ==1:
            print("You chose to Hit...")
            card = gameControl.hit(gameCards)
            print("Your new card is",card)
            print("Your new cards sum =",myPlayer.cardSum)
            if gameControl.bust():
                print("YOU LOST...\nCOMPUTER WILL COLLECT YOUR MONEY...")
                myPlayer.giveUpLosts()
                myPlayer.moneyOwn()
                break #exists the take turns loop back to main loop 
            else:
                continue #goes back to ask player for choices
        elif choice == 2:
            print("Player"+gameControl.stay())

        print("Compuer Cards sum =",gameControl.computerCardSum)
        #Computer playing here
        while True:
            card=gameControl.hit(gameCards,THE_COMPUTER)
            print("Computer hit new card",card)
            print("Compuer new Cards sum =",gameControl.computerCardSum)
            if gameControl.bust(THE_COMPUTER):
                print("YOU WON...\nYou doubled your bid money...")
                myPlayer.collectWinnings()
                myPlayer.moneyOwn()
                break # breaks out of computer turn loop    
            elif gameControl.computerCardSum<myPlayer.cardSum:
                continue # let computer hit again if its card sum less than player'
            else:
                print("Computer "+gameControl.stay())
                print("YOU LOST...\nCOMPUTER WILL COLLECT YOUR MONEY...")
                myPlayer.giveUpLosts()
                myPlayer.moneyOwn()
                break #breaks out of taking turns loop
        break
    #loop to validtae input to play again
    while True:
        try:
            userchoice = int(input("Play again?\n1.YES\n2.NO\n Your number of choice = "))   
        except:
            print("Please choose an appropriate number....")
            continue
        else:
            if userchoice==1 or userchoice ==2:
                break
            print("Please choose an appropriate number....")
            continue
    if userchoice==1:
        if myPlayer.bankRole>0:
            continue
        print("You Do not have enough money to play again!!!!!!!")
        break
    elif userchoice==2:
        break