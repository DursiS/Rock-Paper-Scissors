import r_p_s

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