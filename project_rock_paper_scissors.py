import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Try again?...")

computer_random_number = random.randint(1, 3)

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")


# import random
#
# def game():
#     possible_moves = ["rock", "paper", "scissors"]
#     computer_move = random.choice(possible_moves)
#
#     your_move = input("Choose rock, paper, or scissors: ").lower()
#
#     print(f"The computer chose: {computer_move}")
#     print(f"You chose: {your_move}")
#
#     if your_move not in possible_moves:
#         print("Invalid choice. Please choose rock, paper, or scissors.")
#         return
#
#     if your_move == computer_move:
#         print("It's a tie! No one wins.")
#     elif (
#         (your_move == "rock" and computer_move == "scissors") or
#         (your_move == "scissors" and computer_move == "paper") or
#         (your_move == "paper" and computer_move == "rock")
#     ):
#         print("You win!")
#     else:
#         print("The computer wins!")
#
# game()
