import random
#takes the user choice from the input choice lists
user_action = input("Enter a choice(rock, paper, scissors):\t")

#Make the computer choice by using random.choice() function
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)