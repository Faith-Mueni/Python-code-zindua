#write a program for the rock, paper, scissors game

import random
user_action = input ("enter a choice (rock,paper, scissors):")

possible_action = ["rock","paper","scissors"]
computer_action = random.choice (possible_action)

print (f"\n you chose {user_action}, computer chose {computer_action}")

if user_action ==computer_action:
    print (f"both players selected {user_action}, It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("rock smashes scissors!You win!")
    else:
        print ("paper covers rock!You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("paper covers rock! You win!")
    else:
        print ("scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("rock smashes scissors! yOU lose.")

print (f"\n you chose {rock}, computer chose {scissors}")
