import random
#takes the user choice from the input choice lists
user_action = input("Enter a choice(rock, paper, scissors):\t")
#Make the computer choice by using random.choice() function
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")