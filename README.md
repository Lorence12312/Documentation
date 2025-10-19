ROCK-PAPER-SCISSOR DOCUMENTATION PER LINE 
Import random – imports Python’s random module so the program can make random choices (used for 			the computer move)

import sys
Imports the sys module so we can call sys.stdout.flush() to force immediate printing (used in the thinking animation).

import time
Imports time so the program can pause execution briefly with time.sleep() to create animation/timing effects.
from colorama import Fore, Style, init
Imports parts of the colorama package: Fore (foreground color constants), Style (text style constants), and init() (initialization function). These are used to color terminal output.
init(autoreset=True)
Initializes colorama and sets autoreset=True so color changes apply only to the printed string and automatically reset afterward (prevents later prints from inheriting the color).
mylist = ["rock", "paper", "scissor"]
Creates a list named mylist containing the three valid game choices. Both player and computer selections are checked against this.
wins = 0
Initializes the player's win counter to zero.
losses = 0
Initializes the player's loss counter to zero.
draws = 0
Initializes the draw/tie counter to zero.
def thinking_animation():
Defines a function named thinking_animation. Calling this runs the block indented beneath it.
print("\nComputer is thinking", end="")
Prints "Computer is thinking" preceded by a newline. end="" prevents print from adding a newline at the end so the dots print on the same line.
for i in range(3):
A loop that will iterate 3 times (i = 0,1,2). Used to print three dots one at a time.
time.sleep(0.3)
Pauses program execution for 0.3 seconds to create the dot-by-dot animation timing.
print(".", end="")
Prints a dot without a newline so successive dots appear on the same line.
sys.stdout.flush()
Forces the print buffer to flush immediately; ensures each dot is shown right away rather than buffered.
time.sleep(0.3)
After the loop finishes, waits an additional 0.3 seconds before moving on (small pause).
print("\n")
Prints a newline, moving the cursor to the next line and adding an empty line for spacing.
def print_gui(player, computer, result):
Defines print_gui, a function that accepts the player's choice, the computer's choice, and the result string to display a formatted round summary.
print("\n" + "="*40)
Prints a newline and then a line of 40 equals signs — a top border for the GUI block.
print("ROCK–PAPER–SCISSORS".center(40))
Prints the title centered inside 40 characters width.
print("=" * 40)
Prints another 40 equal signs (bottom of the header).
print(f"You: {player.upper():<10} | Computer: {computer.upper()}")
Prints a line showing the player's and computer's choices.
•	player.upper() / computer.upper() converts choices to uppercase for emphasis.
•	:<10 left-justifies the player's text within 10 characters so the column lines up.
print("-"* 40)
Prints a 40-character dash line as a separator.
if "Win" in result:
Checks whether the substring "Win" appears in the result string. This determines color and alignment used next.
print(Fore.GREEN + result.center(40))
If the result includes "Win", prints it centered within 40 characters in green (Fore.GREEN).
elif "Lose" in result:
Else-if checks whether "Lose" appears in the result.
print(Fore.RED + result.center(40))
If "Lose", prints the centered result in red.
else:
Fallback for results that aren't "Win" or "Lose" — typically draws.
print(Fore.MAGENTA + result.center(40))
Prints the result centered in magenta for draws or other messages.
print("-" * 40)
Prints another 40-character dash separator.
print(f"🏆 Score → Wins: {wins} | Losses: {losses} | Draws: {draws}")
Prints the current scoreboard using the global wins, losses, and draws variables.
print("=" * 40 + "\n")
Prints a closing line of equals signs plus an extra newline to space after the GUI.
print(Fore.CYAN + "🎮 Welcome to Rock–Paper–Scissors (Best of 5)!")
Prints a colorful welcome message in cyan as soon as the script runs.
print(Fore.YELLOW + "First to 3 wins becomes the Champion 🏅")
Prints the rules/instructions in yellow.
print(Fore.WHITE + "Type 'quit' to exit anytime.\n")
Prints a hint about how to quit in white, followed by a newline for spacing.
while True:
Starts an infinite loop; gameplay repeats until a break occurs (when someone reaches 3 wins or player types 'quit').
playerChoice = str(input("Enter your choice (rock, paper, scissor) or 'quit' to exit: ")).lower()
Prompts the user for input, converts the input to a string, then lowercases it so the program treats ROCK, Rock, etc. the same as rock. The result is stored in playerChoice.
thinking_animation()
Calls the thinking_animation() function to show the computer “thinking” animation.
computerChoice = random.choice(mylist)
Randomly picks one item from mylist and stores it in computerChoice- the computer’s move.
if playerChoice == "quit":
Checks if the player typed "quit" to end the game.
print("Game Over 🏁")
If quitting, prints a game-over message.
print(f"Final Score → Wins: {wins} | Losses: {losses} | Draws: {draws}")
Prints the final scoreboard before exiting.
break
Breaks out of the while True loop, ending the program.
if playerChoice not in mylist:
Checks whether the player typed a valid move (rock/paper/scissor). If not, handle invalid input.
print("Invalid input ⚠️ Try again.\n")
Informs the user their input was invalid and asks them to try again.
continue
Skips the remainder of this loop iteration and returns to the top of the while True loop to prompt again.
if "rock" in playerChoice:
Checks whether the string "rock" appears in the player input. This guards against slight extra words but can also accept unintended inputs that contain "rock".
if computerChoice == "rock":
If computer also picked "rock":
print("The Computer picks", computerChoice)
Prints what the computer picked.
result = "Draw!"
Sets the result string to "Draw!".
draws += 1
Increments the global draws counter by 1.
elif computerChoice == "paper":
If computer picked "paper":
print("The Computer picks", computerChoice)
Prints computer choice.
result = "You Lose"
Sets the result to "You Lose".
losses += 1
Increments the losses counter.
elif computerChoice == "scissor":
If computer picked "scissor":
print("The Computer picks", computerChoice)
Prints computer choice.
result = "You Win"
Sets result to "You Win".
wins += 1
Increments the wins counter.
elif "scissor" in playerChoice:
If the player’s input contains "scissor", this block runs. (Same substring approach as rock.)
if computerChoice == "rock":
If computer picked rock:
print("The Computer picks", computerChoice)
Prints computer choice.
result = "You Lose"
Player loses.
losses += 1
Increment losses.
elif computerChoice == "paper":
If computer picked paper:
print("The Computer picks", computerChoice)
Prints.
result = "You Win"
Player wins.
wins += 1
Increment wins.
elif computerChoice == "scissor":
If both picked scissor:
print("The Computer picks", computerChoice)
Prints.
result = "Draw!"
Result is draw.
draws += 1
Increment draws.
elif "paper" in playerChoice:
If player's input contains "paper", execute this block.
if computerChoice == "rock":
If computer picked rock:
print("The Computer picks", computerChoice)
Prints.
result = "You Win"
Player wins.
wins += 1
Increment wins.
elif computerChoice == "paper":
If computer picked paper:
print("The Computer picks", computerChoice)
Prints.
result = "Draw!"
Draw.
draws += 1
Increment draws.
elif computerChoice == "scissor":
If computer picked scissor:
print("The Computer picks", computerChoice)
Prints.
result = "You Lose"
Player loses.
losses += 1
Increment losses.
print("invalid string")
Prints that the string is invalid.
break
Breaks the loop and ends the program.
print_gui(playerChoice, computerChoice, result)
Calls the print_gui function to display a formatted round summary with the updated score.
if wins == 3:
Checks if the player has reached 3 wins.
print("You are the Champion! \n")
If yes, print champion message.
print(f"Final Score → Wins: {wins} | Losses: {losses} | Draws: {draws}")
Prints final scoreboard.
break
Ends the game loop.
elif losses == 3:
Checks if the computer has reached 3 wins (i.e., player has 3 losses).
print(" The Computer is the Champion! \n")
Prints computer champion message (note leading space at start of string).
print(f"Final Score → Wins: {wins} | Losses: {losses} | Draws: {draws}")
Prints final scoreboard.
break
Ends the game loop.



