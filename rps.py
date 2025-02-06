#value = input('Please enter a value')
#print(value)
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

#print (RPS(2))
#print (RPS.ROCK)
#print (RPS['ROCK'])
#print (RPS.ROCK.value)
#sys.exit()

playagain = True

while playagain: 

   
    playerchoice =input("\nEnter...\n1 for rock\n2 for paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player <1 or player >3:
        sys.exit("you must enter 1, 2, or 3.")

    computerchoice = random.choice("123")
    computer =int(computerchoice)

    

    print ("\nyou choose "+ str(RPS(player)).replace("RPS.", '') + ".")
    print ("python choose "+ str(RPS(computer)).replace("RPS.", '') + ".\n")


    if player == 1 and computer == 3:
        print ("you win!")
    elif player == 2 and computer == 1:
        print ("you win!")
    elif player == 3 and computer == 2:
        print ("you win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("python win!")
    
    playagain = input("\nPlay Again? \nY for yes or \nQ to Quit. \n\n")
    
    if playagain.lower() == "y":
        continue
    else:
        print ("\nThank you for playing!\n")
        playagain =False

sys.exit("Bye!")