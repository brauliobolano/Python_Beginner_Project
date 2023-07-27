# r > s, p > r, s > p
import random


def play():
    user_choice = input(" Select one choice: 'r' for rock, 'p' for paper, 's' for scissor: ")
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        return "Tie"
    elif win(user_choice, computer_choice):
        return "You are the Champion\n        Fredy Mercury"

    return "You died AMIGO"

# r > s, p > r, s > p


def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
