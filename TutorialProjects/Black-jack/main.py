import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

computer_cards = []

user_cards = []


for card in cards:
    if len(user_cards) < 2:
        user_cards.append(random.choice(cards))
    elif len(computer_cards) < 2:
        computer_cards.append(random.choice(cards))

game_is_on = True

while game_is_on:
    for card in cards:
        if len(user_cards) < 2:
            user_cards.append(random.choice(cards))
        elif len(computer_cards) < 2:
            computer_cards.append(random.choice(cards))


    take_card = input(f"Your cards are {user_cards}. Do you wish to take another card? (Y/N) ").lower()

    if take_card == "y":
        user_cards.append(random.choice(cards))
    else:
        computer_cards.append(random.choice(cards))

    sum_user_cards = sum(user_cards)
    sum_computer_cards = sum(computer_cards)

    if sum_user_cards > 21 and 11 in user_cards:
        for i in range(len(user_cards)):
            if user_cards[i] == 11:
                user_cards[i] = 1
                sum_user_cards = sum(user_cards)
    if sum_computer_cards > 21:
        for i in range(len(computer_cards)):
            if computer_cards[i] == 11:
                computer_cards[i] = 1
                sum_computer_cards = sum(computer_cards)
    next_round = input(f"The sum of your cards are {sum_user_cards} do you wish to continue another round?(Y/N) ").lower()

    if sum_user_cards > 21 and 11 not in user_cards or next_round == "n" and sum_user_cards < sum_computer_cards <= 21:
        if sum_user_cards > 21:
            print("You can't continue the sum of your cards is > than 21")
        print("You lose... :(")

    elif sum_computer_cards > 21 and 11 not in computer_cards or next_round == "n" \
            and sum_computer_cards < sum_user_cards <= 21:
        print("You WIN !!!")

    repeat = input(f"The sum of your cards is {sum_user_cards} and the sum of the "
                   f"computer cards is {sum_computer_cards}. Do you wish to play another round?(Y/N) ").lower()

    if repeat == "y":
        user_cards = []
        computer_cards = []
        continue
    else:
        print("...Exiting game")
        break
