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

