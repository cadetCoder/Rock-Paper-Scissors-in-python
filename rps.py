#use import random when computer plays 
import random

while True:
#takes the user choice from the input choice lists
  user_action = input("Enter a choice(rock, paper, scissors):\t")
  #Make the computer choice by using random.choice() function
  possible_actions = ["rock", "paper", "scissors"]
  computer_action = random.choice(possible_actions)
  print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

  #Determine the winner of the game
  if user_action == computer_action:
      print(f"Both players selected {user_action}. It's a tie!")
  elif user_action == "rock":
      if computer_action == "scissors":
          print("Rock smashes scissors! You win!")
      else:
          print("Paper covers rock! You lose.")
  elif user_action == "paper":
      if computer_action == "rock":
          print("Paper covers rock! You win!")
      else:
          print("Scissors cuts paper! You lose.")
  elif user_action == "scissors":
      if computer_action == "paper":
          print("Scissors cuts paper! You win!")
      else:
          print("Rock smashes scissors! You lose.")
#play several games in a row
  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
      break