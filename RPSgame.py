import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def get_user_choice():
    while True:
        print("Enter your choice:")
        print("1. \N{Raised Fist} Rock")
        print("2. \N{Page Facing Up} Paper")
        print("3. \N{Black Scissors} Scissors")
        user_input = input("Enter the number of your choice: ")
        if user_input in ["1", "2", "3"]:
            if user_input == "1":
                return "rock"
            elif user_input == "2":
                return "paper"
            else:
                return "scissors"
        else:
            print("Invalid choice! Please choose again.")

def display_result(player_choice, computer_choice, result, user_score, computer_score):
    print(f"You chose {player_choice}, and the computer chose {computer_choice}.")
    print(result)
    print(f"Your score: {user_score}, Computer's score: {computer_score}")

def play_game():
    user_score = 0
    computer_score = 0
    print("Let's play Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = determine_winner(user_choice, computer_choice)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        display_result(user_choice, computer_choice, result, user_score, computer_score)
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()
