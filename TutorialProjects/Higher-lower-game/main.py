from game_data import data
from art import logo, vs
import random

print(logo)


def comparator(my_choice, a, b):
    score = 0
    while True:
        if my_choice == "a" and a["follower_count"] > b["follower_count"]:
            score += 1
            print(f"\n\n\nCongratulations! That's right, your current score is: {score}\n--------")
            return a

        elif my_choice == "b" and a["follower_count"] < b["follower_count"]:
            score += 1
            print(f"\n\n\nCongratulations! That's right, your current score is: {score}\n--------")
            return b

        else:
            print("Sorry that's wrong.\n...closing game.....")
            exit()


option_a = (random.choice(data))


game_is_on = True


while game_is_on:
    option_b = (random.choice(data))
    if option_b == option_a:
        while option_b == option_a:
            option_b = (random.choice(data))
    else:
        print(f'{option_a["name"]}. \n{option_a["description"]} from {option_a["country"]}\n--------')
        print(vs)
        print(f'{option_b["name"]}. \n{option_b["description"]} from {option_b["country"]}\n--------')

        choice = input(f'Who has more followers? '
                       f'Write "A" for {option_a["name"]} or "B" for {option_b["name"]}?').lower()

        while choice != "a" and choice != "b":
            print(f"\n¿'{choice.upper()}'? what is ¿'{choice}'!?!\nIt isn't difficult ... 'A' or 'B'... "
                  f"\nTrust yourself ...I'm sure you can do it... \n(Pfaff stupid human)... :(\n")

            choice = input(f'Who has more followers? '
                           f'Write "A" for {option_a["name"]} or "B" for {option_b["name"]}?').lower()
        option_a = comparator(choice, option_a, option_b)
