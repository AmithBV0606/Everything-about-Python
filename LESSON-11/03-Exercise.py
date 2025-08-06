# Improved Rock, paper , scissors game :

import sys
import random
from enum import Enum

game_count = 0


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

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🏆 You Win!!"
        elif player == 2 and computer == 1:
            return "🏆 You Win!!"
        elif player == 3 and computer == 2:
            return "🏆 You Win!!"
        elif player == computer:
            return "😳 Tie game!!"
        else:
            return "🐍 Python Wins!!"

    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count
    game_count += 1

    print("\nGame Count : " + str(game_count))

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
