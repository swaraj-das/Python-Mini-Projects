import random

def user_choice():
    choices = {"r": "rock", "p": "paper", "s": "scissors", "0": "quit"}
    user_choice = input("Enter your choice (R: rock, P: paper, S: scissors, 0: to quit): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter R, P, S, or 0 to quit: ").lower()
    return choices[user_choice]

def comp_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = user_choice()
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        computer_choice = comp_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
    
play_game()
