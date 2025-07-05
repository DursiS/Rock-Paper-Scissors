"""Functions for the Rock-Paper_Scissors game."""
import random
num = 0
choice = ""
opponent_choice = ""

def play_again():
    """Returns the user's choice about weather they'd play or not."""
    again = ""
    valid_again = ["y", "n", "yes", "no"]
    again = input("Would you like to play again? (y/n) ").lower()
    
    while again not in valid_again:
        print("Invalid choice. Please try again.")
        again = input("\n Would you like to play again? (y/n) ").lower()
    
    if again in ["y", "yes"]:
        return True
    elif again in ["n", "no"]:
        return False


def make_user_choice():
    """Returns the user's choice of rock, paper, or scissors."""
    choice = ""
    valid_choices = ["rock", "paper", "scissors"]
    choice = input("Choose one: rock, paper, or scissors? ").lower()
    
    while choice not in valid_choices:
        print("Invalid choice. Please try again.")
        choice = input("Choose one: rock, paper, or scissors? ").lower()
    
    return choice
    

def make_computer_choice():
    """Returns the computer's random choice of rock, paper, or scissors."""
    num = random.randint(1,3)
    if num == 1:
        return "scissors"
    if num == 2:
        return "paper"
    if num == 3:
        return "rock"

def wins_matchup(choice, opponent_choice):
    """Returns True if the first player's choice wins over their opponent.

    Choices can be rock, paper, or scissors. Assumes the choices are different.
    """
    if choice == "rock" and opponent_choice == "paper":
        return False
    elif choice == "paper" and opponent_choice == "rock":
        return True
    elif choice == "paper" and opponent_choice == "scissors":
        return False 
    elif choice == "scissors" and opponent_choice == "paper":
        return True
    elif choice == "rock" and opponent_choice == "scissors":
        return True
    elif choice == "scissors" and opponent_choice == "rock":
        return False


def format_score(user_score, computer_score):
    """Returns a formatted version of the players's current scores."""
    return ">> Score: " + str(user_score) + "-" + str(computer_score) + "\n"
    
def running_score(user_score, computer_score):
    """Returns a formatted version of the running total of scores."""
    user_win = 0
    computer_win = 0
    if user_score >= 2:
        user_win += 1
    elif computer_score >= 2:
        computer_win += 1
    return ">> Total Score: " + str(user_win) + "-" + str(computer_win) + "\n"
        
def visual(choice, opponent_choice):
    if choice == "rock" and opponent_choice == "paper":
        return print(r_p)
    elif choice == "rock" and opponent_choice == "rock":
        return print(r_r)
    elif choice == "rock" and opponent_choice == "scissors":
        return print(r_s)
    elif choice == "scissors" and opponent_choice == "paper":
        return print(s_p)
    elif choice == "scissors" and opponent_choice == "rock":
        return print(s_r)
    elif choice == "scissors" and opponent_choice == "scissors":
        return print(s_s)
    elif choice == "paper" and opponent_choice == "paper":
        return print(p_p)
    elif choice == "paper" and opponent_choice == "rock":
        return print(p_r)
    elif choice == "paper" and opponent_choice == "scissors":
        return print(p_s)
       
        
        
        
# Rock Paper Scissors ASCII Art by @wynand1004


#Scissor combinations

s_s = ("""
    _______                    _______
---'   ____)____          ____(____   '---
          ______)        (______
       __________)      (__________
      (____)                  (____)
---.__(___)                    (___)__.---
     SCISSORS (you)            SCISSORS
""")

s_r = ("""
    _______                  _______
---'   ____)____            (____   '---
          ______)          (_____)
       __________)         (_____)
      (____)                 (____)
---.__(___)                   (___)__.---
   SCISSORS (you)                ROCK
""")

s_p = ("""
    _______                  _______
---'   ____)____            (____   '---
          ______)          (_____)
       __________)         (_____)
      (____)                   (____)
---.__(___)                     (___)__.---
   SCISSORS (you)                PAPER
""")

#Rock combinations
r_r = ("""
    _______                _______
---'   ____)              (____   '---
      (_____)            (_____)
      (_____)            (_____)
      (____)              (____)
---.__(___)                (___)__.---
     ROCK (you)               ROCK
""")

r_p = ("""
    _______                _______
---'   ____)____          (____   '---
          ______)        (_____)
         _______)        (_____)
        _______)         (____)
---.__________)           (___)__.---
     ROCK (you)               PAPER
""")

r_s = ("""
    _______                _______
---'   ____)              (____   '---
      (_____)            (_____)
      (_____)            (_____)
      (____)                (__)
---.__(___)                  (__).---
     ROCK (you)             SCISSORS
""")

#Paper combinations
p_p = ("""
    _______                        _______
---'   ____)____            ______(____   '---
          ______)          (______
         _______)          (_______
        _______)           (_______
---.__________)              (__________.---
       PAPER (you)              PAPER
""")

p_r = ("""
    _______                _______
---'   ____)____          (____   '---
          ______)        (_____)
         _______)        (_____)
        _______)         (____)
---.__________)           (___)__.---
       PAPER (you)            ROCK
""")

p_s = ("""
    _______                _______
---'   ____)____          (____   '---
          ______)        (_____)
         _______)        (_____)
        _______)             (__)
---.__________)               (__).---
       PAPER (you)            SCISSORS
""")

