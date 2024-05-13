import random

def get_user_choice():
    return input("Enter your choice (Rock, Paper, Scissors, Lizard, Spock): ").lower()

def get_computer_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or
        (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or
        (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or
        (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or
        (user_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock"))
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()
