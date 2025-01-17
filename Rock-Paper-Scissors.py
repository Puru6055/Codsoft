import random

def RPS():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    user = input("Do you choose rock, paper or scissors? ").lower()
    while user not in choices:
        user = input("Please enter rock, paper, or scissors: ").lower()

    print("Computer chose " + computer)

    if user == computer:
        return "It's a tie!"
    if user == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win"
        else:
            return "Paper covers rock! You lose."
    if user == "paper":
        if computer == "rock":
            return "Paper covers rock! You win"
        else:
            return "Scissors cuts paper! You lose."
    if user == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win"
        else:
            return "Rock smashes scissors! You lose."

print("Let's play Rock-Paper-Scissors!")
print(RPS())

play_again = input("wantS to play again? (yes/no): ").lower()
while play_again not in ["yes", "no"]:
    play_again = input("Please enter yes or no: ").lower()

if play_again == "yes":
    print(RPS())
else:
    print("Thanks for playing here")