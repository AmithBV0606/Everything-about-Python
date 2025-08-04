# Rock, paper and scissors game :
import sys
import random
from enum import Enum

print('==================================================================')

# Input players will be in string :
playerChoice = input(
    "Enter... \n1 for Rock, \n2 for paper, or \n3 for scissors:\n\n")

# Convert the string input to number :
player = int(playerChoice)

# Check if the entered number by the user exceeds our range :
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2 or 3.")

# Then make the computer choose the numbers from 1 to 3 :
computerChoice = random.choice("123")

# Convert the computer's choice to number :
computer = int(computerChoice)

# Create an Enums for storing the values :


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# Display what user and computer have chosen :
print('')
print('You chose ' + str(RPS(player)).replace("RPS.", "") + ".")
print('Python chose ' + str(RPS(computer)).replace("RPS.", "") + ".")
print('')

# Compare the values between the user and computer :
if player == 1 and computer == 3:
    print("🏆 You Win!!")
elif player == 2 and computer == 1:
    print("🏆 You Win!!")
elif player == 3 and computer == 2:
    print("🏆 You Win!!")
elif player == computer:
    print("😳 Tie game!!")
else:
    print("🐍 Python Wins!!")


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)
# sys.exit()
