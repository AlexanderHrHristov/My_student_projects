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

#CHAT GPT v1
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

#CHAT GPT v2
# import random
#
# rock = "Rock"
# paper = "Paper"
# scissors = "Scissors"
#
# # ASCII art for the game elements
# rock_image = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
#
# paper_image = """
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# """
#
# scissors_image = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
#
# elements = [rock, paper, scissors]
# element_images = [rock_image, paper_image, scissors_image]
#
# player_choice = input("Choose [r]ock, [p]aper, [s]cissors: ")
#
# if player_choice == "r":
#     player_choice = rock
# elif player_choice == "p":
#     player_choice = paper
# elif player_choice == "s":
#     player_choice = scissors
# else:
#     raise SystemExit("Invalid input. Try again?...")
#
# computer_choice = random.choice(elements)
#
# print(f"\nYou chose:\n{element_images[elements.index(player_choice)]}")
# print(f"\nThe computer chose:\n{element_images[elements.index(computer_choice)]}")
#
# if player_choice == computer_choice:
#     print("It's a draw!")
# elif (player_choice == rock and computer_choice == scissors) or \
#      (player_choice == paper and computer_choice == rock) or \
#      (player_choice == scissors and computer_choice == paper):
#     print("You win!")
# else:
#     print("You lose!")
