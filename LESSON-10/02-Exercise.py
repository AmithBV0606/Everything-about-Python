# Improved Rock, paper , scissors game :

import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerChoice = input(
        "Enter... \n1 for Rock, \n2 for paper, or \n3 for scissors:\n\n")

    if playerChoice not in ["1", "2", "3"]:
        print("You must enter 1, 2 or 3.")
        print("========================START==============================")
        return play_rps()

    player = int(playerChoice)

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

    print("\nPlay again?")

    while True:
        playAgain = input("\nY for Yes \nQ to Quit\n")
        if playAgain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playAgain.lower() == "y":
        print("========================START==============================")
        return play_rps()
    else:
        print("\n🎉 🎉 🎉 🎉")
        print("Thank you for playing!\n")
        print("=========================END==============================")
        sys.exit("Bye! 👋👋👋👋")


play_rps()
