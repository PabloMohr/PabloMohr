import random

user_cards = []
pc_cards = []


def sum_cards(cards_sum):
    summed_cards = sum(cards_sum)
    return summed_cards


def deal_card(card_append):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    if len(card_append) < 2:
        for card in range(2):
            card_append.append(random.choice(cards))
    else:
        card_append.append(random.choice(cards))

    if sum_cards(card_append) > 21 and 11 in card_append:
        card_append.remove(11)
        card_append.append(1)


game_is_on = True

while game_is_on:
    if len(user_cards) < 2 or len(pc_cards) < 2:
        deal_card(user_cards)
        deal_card(pc_cards)

    take_card = input(f"Your cards are {user_cards} do you wish to take a card?(Y/N) ").lower()

    if take_card == "y":
        deal_card(user_cards)
    else:
        continue

    if sum_cards(pc_cards) < 16:
        deal_card(pc_cards)
    else:
        continue

    show_cards = input(f"The sum of your cards is {sum_cards(user_cards)}. Do you want to show cards?(Y/N) ").lower()

    if sum_cards(pc_cards) > 21 or sum_cards(user_cards) > 21:
        show_cards = "y"

    if show_cards == "y":
        if sum_cards(user_cards) > 21 and sum_cards(pc_cards) > 21:
            print("...\n....\n:( Both of you are too greedy. It's a draw!!")

        elif sum_cards(user_cards) > sum_cards(pc_cards) or sum_cards(pc_cards) > 21:
            print("You Win!!!")

        elif sum_cards(pc_cards) > sum_cards(user_cards) or sum_cards(user_cards) > 21:
            print("You Lose... :(")


        play_again = input(f"-> Your cards are {user_cards} and your score is: {sum_cards(user_cards)}. \n"
                           f"-> The computers cards are {pc_cards} and his score is: {sum_cards(pc_cards)}.\n"
                           f"-> Do you want to repeat?(Y/N) ").lower()
        if play_again == "y":
            user_cards = []
            pc_cards = []
            deal_card(user_cards)
            deal_card(pc_cards)
        else:
            print("...Closing game...")
            break
    else:
        continue
