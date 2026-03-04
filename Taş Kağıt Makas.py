import time
import random
while True:

    time.sleep(1)
    print("\nEnter a choice between rock, paper and scissors.")
    player_action = input("Your choice: ")
    
    possible_actions = ("Rock", "Paper", "Scissors")
    computer_action = random.choice(possible_actions)
    print("Computer choice: ", computer_action)
    
    if player_action == computer_action:
        print("Draw.")

    elif player_action == "Rock" or "rock" or "ROCK":
        if computer_action == "Paper":
            print("Paper covers rock. \nComputer win.")

        elif computer_action == "Scissors":
            print("Rock smashes scissors. \nPlayer win.")

    elif player_action == "Paper" or "paper" or "PAPER":
        if computer_action == "Rock":
            print("Paper covers rock. \nPlayer win.")
    
        elif computer_action == "Scissors":
            print("Scissors cuts paper. \nComputer win.")

    elif player_action == "Scissors" or "scissors" or "SCİSSORS":
        if computer_action == "Rock":
            print("Rock smashes scissors. \nComputer win.")

        elif computer_action == "Paper":
            print("Scissors cuts paper. \nPlayer win.")

    time.sleep(1)
    play_again = input("Do you want to play again? \nType yes to continue, type no to finish.\n ")

    if play_again.lower() !="yes":
        if play_again.lower() !="YES":
            if play_again.lower() !="Yes":
                if play_again.lower() !="y":
                    break

    
