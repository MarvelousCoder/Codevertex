import random

options = ("rock", "paper", "scissors")

continuation = True

user_win = 0
computer_win = 0

while continuation:
    user = None

    while user not in options:
        user = input("Enter a choice (rock, paper, scissors):\n")
        user = user.lower()

        if user not in options:
            print("Invalid input. Please enter rock, paper, or scissors.\n")
            continue  # Skip to the next iteration of the loop

        computer = random.choice(options)

        print(f"User: {user}")
        print(f"Computer: {computer}")

        if user == computer:
            print("It's a tie!!")
        elif user == "scissors" and computer == "paper":
            print("Scissors cuts paper, user wins!!")
            user_win += 1
        elif user == "paper" and computer == "rock":
            print("Paper covers rock, user wins!!")
            user_win += 1
        elif user == "rock" and computer == "scissors":
            print("Rock crushes scissors, user wins!!")
            user_win += 1
        else:
            print("Computer wins!!")
            computer_win += 1

        print(f"Current wins: User: {user_win} | Computer: {computer_win}")
        playagain = input("Do you want to play again? (yes / no):\n")
        playagain = playagain.lower()
        if playagain != "yes":
            continuation = False

print("Thank you for playing this game!")
