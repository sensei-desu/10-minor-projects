import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    print("=== Rock, Paper, Scissors ===")
    
    while True:
        user = input("\nChoose (rock/paper/scissors or 'q' to quit): ").lower().strip()
        
        if user == 'q':
            print("Thanks for playing! Bye!")
            break

        if user not in choices:
            print("Invalid choice! Please pick rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    play_game()
