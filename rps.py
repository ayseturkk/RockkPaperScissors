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

print("")
playerchoice =input("Enter...\n1 for rock\n2 for paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player <1 or player >3:
    sys.exit("you must enter 1, 2, or 3.")

computerchoice = random.choice("123")
computer =int(computerchoice)

print("")

print ("you choose "+ str(RPS(player)).replace("RPS.", '') + ".")
print ("python choose "+ str(RPS(computer)).replace("RPS.", '') + ".")

print("")

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
