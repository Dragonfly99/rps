def rps():
    print("Hello player 1! What would you like to play?")
    move1 = input()
    print("Now player 2, what is your move?")
    move2 = input()

    if(move1 == 'rock' and move2 == 'scissors'):    
        print("Rock beats scissors!")

    elif(move1 == 'scissors' and move2 == 'rock'):
        print("Rock beats scissors!")

    elif(move1 == 'scissors' and move2 == 'paper'):
        print("Scissors beats paper!")

    elif(move1 == 'paper' and move2 == 'scissors'):
        print("scissors beats paper!")
    
    elif(move1 == 'paper' and move2 == 'rock'):
        print("Paper beats rock!")
    
    elif(move1 == 'rock' and move2 == 'paper'):
        print("Paper beats rock!")

    elif(move1 == 'rock' and move2 == 'rock'):
        print("Rock and rock. A draw!")

    elif(move1 == 'paper' and move2 == 'paper'):
        print("Paper and paper. A draw!")

    elif(move1 == 'rock' and move2 == 'paper'):
        print("Scisoors and scissors. A draw!")
    else: 
        print("Hey, what game are you plaing?!")

rps()
