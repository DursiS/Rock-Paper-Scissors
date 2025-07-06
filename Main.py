import r_p_s

user_score = 0
computer_score = 0
running_score = 0


# Best of 3 rounds, so first to 2 points.
while user_score < 2 and computer_score < 2:
    choice = r_p_s.make_user_choice()
    opponent_choice = r_p_s.make_computer_choice()
    r_p_s.visual(choice, opponent_choice)

    # Restarts if a tie. Does not update score.
    if choice == opponent_choice:
        print("It's a tie!")
        continue

    if r_p_s.wins_matchup(choice, opponent_choice):
        print("You win!")
        user_score = user_score + 1
    else:
        print("Computer wins!")
        computer_score = computer_score + 1

    print(r_p_s.format_score(user_score, computer_score))
    
    #Adds to the running score of all games
    if user_score >= 2:
        running_score += 1
    elif computer_score >= 2:
        running_score += 1
        
    print(r_p_s.running_score(user_score, computer_score))
    
    
again_choice = r_p_s.play_again()

# Plays again if True
if again_choice == True:
    user_score = 0
    computer_score = 0
    while user_score < 2 and computer_score < 2:
        choice = r_p_s.make_user_choice()
        opponent_choice = r_p_s.make_computer_choice()
        r_p_s.visual(choice, opponent_choice)

        # Restarts if a tie. Does not update score.
        if choice == opponent_choice:
            print("It's a tie!")


        if r_p_s.wins_matchup(choice, opponent_choice):
            print("You win!")
            user_score = user_score + 1
        else:
            print("Computer wins!")
            computer_score = computer_score + 1

        print(r_p_s.format_score(user_score, computer_score))
        
        #Adds to the running score of all games
        if user_score >= 2:
            running_score += 1
        elif computer_score >= 2:
            running_score += 1

