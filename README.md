import random
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

#rock paper and scissor list
mylist = ["rock", "paper", "scissor"]

#score counters
wins = 0
losses = 0
draws = 0

#tthinking animation
def thinking_animation():
    print("\nComputer is thinking", end="")
    for i in range(3):
        time.sleep(0.3)
        print(".", end="")
        sys.stdout.flush()
    time.sleep(0.3)
    print("\n")

#GUI like
def print_gui(player, computer, result):
    print("\n" + "="*40)
    print("ROCK–PAPER–SCISSORS".center(40))
    print("=" * 40)
    print(f"You: {player.upper():<10}  |  Computer: {computer.upper()}")
    print("-"* 40)
    if "Win" in result:
        print(Fore.GREEN + result.center(40))
    elif "Lose" in result:
        print(Fore.RED + result.center(40))
    else:
        print(Fore.MAGENTA + result.center(40))
    print("-" * 40)
    print(f"🏆 Score → Wins: {wins} | Losses: {losses} | Draws: {draws}")
    print("=" * 40 + "\n")

#introduction message
print(Fore.CYAN + "🎮 Welcome to Rock–Paper–Scissors (Best of 5)!")
print(Fore.YELLOW + "First to 3 wins becomes the Champion 🏅")
print(Fore.WHITE + "Type 'quit' to exit anytime.\n")

#loop so that the game runs indefinitely until user wants to end
while True:
    #user inputs rock, paper scissor
    #.lower() makes sure that ROCK, and rOcK is a valid input
    playerChoice = str(input("Enter your choice (rock, paper, scissor) or 'quit' to exit: ")).lower()
    thinking_animation()
    computerChoice = random.choice(mylist)

    if playerChoice == "quit":
        print("Game Over 🏁")
        print(f"Final Score → Wins: {wins} | Losses: {losses} | Draws: {draws}")
        break
    if playerChoice not in mylist:
        print("Invalid input ⚠️ Try again.\n")
        continue

    #Player Chooses ROCK
    if "rock" in playerChoice:
        #Computer picks rock
        if computerChoice == "rock":
            print("The Computer picks", computerChoice)
            result = "Draw!"
            draws += 1
        #Computer picks Paper
        elif computerChoice == "paper":
            print("The Computer picks", computerChoice)
            result = "You Lose"
            losses += 1
        #computer picks Scissor
        elif  computerChoice == "scissor":
            print("The Computer picks", computerChoice)
            result = "You Win"
            wins += 1
    # Player Chooses scissor
    elif "scissor" in playerChoice:
        if computerChoice == "rock":
            print("The Computer picks", computerChoice)
            result = "You Lose"
            losses += 1
        elif computerChoice == "paper":
            print("The Computer picks", computerChoice)
            result = "You Win"
            wins += 1
        elif  computerChoice == "scissor":
            print("The Computer picks", computerChoice)
            result = "Draw!"
            draws += 1
    # Player Chooses paper
    elif "paper" in playerChoice:
        if computerChoice == "rock":
            print("The Computer picks", computerChoice)
            result = "You Win"
            wins += 1
        elif computerChoice == "paper":
            print("The Computer picks", computerChoice)
            result = "Draw!"
            draws += 1
        elif  computerChoice == "scissor":
            print("The Computer picks", computerChoice)
            result = "You Lose"
            losses += 1

    #this calls to print GUI
    print_gui(playerChoice, computerChoice, result)

    if wins == 3:
        print("You are the Champion! \n")
        print(f"Final Score → Wins: {wins} | Losses: {losses} | Draws: {draws}")
        break
    elif losses == 3:
        print(" The Computer is the Champion! \n")
        print(f"Final Score → Wins: {wins} | Losses: {losses} | Draws: {draws}")
        break
