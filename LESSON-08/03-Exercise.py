# Improved Rock, paper , scissors game :

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playAgain = True

while playAgain:
    playerChoice = input(
        "Enter... \n1 for Rock, \n2 for paper, or \n3 for scissors:\n\n")

    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3.")

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print('')
    print('You chose ' + str(RPS(player)).replace("RPS.", "") + ".")
    print('Python chose ' + str(RPS(computer)).replace("RPS.", "") + ".")
    print('')

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

    playAgain = input("\nPlay again? \nY for Yes \nQ to Quit \n\n")

    if playAgain.lower() == "y":
        print("==========================================================")
        continue
    else:
        print("\n🎉 🎉 🎉 🎉")
        print("Thank you for playing!\n")
        playAgain = False

    print("==========================================================")

sys.exit("Bye! 👋👋👋👋")
