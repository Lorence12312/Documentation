import random

mylist = ["rock", "paper", "scissor"]

while True:
    playerChoice = str(input("enter your thing:"))
    computerChoice = (random.choice(mylist))
    if "rock" in playerChoice:
        if computerChoice == "rock":
            print("The Computer picks", computerChoice)
            computerChoice = False
            while True:
                print("Draw!")
                break
        elif computerChoice == "paper":
            print("The Computer picks", computerChoice)
            computerChoice = False
            while True:
                print("You Lose")
                break
        elif  computerChoice == "scissor":
            print("The Computer picks", computerChoice)
            computerChoice = True
            while True:
                print("You Win")
                break
            
    elif "scissor" in playerChoice:
        if computerChoice == "rock":
            print("The Computer picks", computerChoice)
            computerChoice = False
            while True:
                print("You Lose")
                break
        elif computerChoice == "paper":
            print("The Computer picks", computerChoice)
            computerChoice = True
            while True:
                print("You Win")
                break
        elif  computerChoice == "scissor":
            print("The Computer picks", computerChoice)
            computerChoice = False
            while True:
                print("Draw")
                break
        
    elif "paper" in playerChoice:
        if computerChoice == "rock":
            print("The Computer picks", computerChoice)
            computerChoice = True
            while True:
                print("You Win")
                break
        elif computerChoice == "paper":
            print("The Computer picks", computerChoice)
            computerChoice = False
            while True:
                print("Draw!")
                break
        elif  computerChoice == "scissor":
            print("The Computer picks", computerChoice)
            computerChoice = False
            while True:
                print("You Lose")
                break
    else:
        print("invalid string")
        break
