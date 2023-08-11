import random


def start_new_game():
    global guessed_number
    guessed_number = random.randint(1, 100)
    print(guessed_number)
    print("Welcome to the number guessing game")
    guess = 0

    while True:
        difficulty = input("What difficulty do you prefer? Hard (5 guesses) or Easy (10 guesses)? ").lower()

        if difficulty == "easy":
            guess = 10
            break
        elif difficulty == "hard":
            guess = 5
            break
        else:
            print(f'"{difficulty}" is not an option please select between easy or hard')
            print("-----------------------------------------------\n-----------------------------------------------")
            continue

    return guess


game_is_on = True

guesses = start_new_game()


while game_is_on:
    your_guess = int(input("Guess a number between 1 and 100 "))
    guesses -= 1
    if guesses > 0 and your_guess != guessed_number:
        if your_guess > guessed_number:
            print(f"The number you chose is to high. You have {guesses} more attempts. Try again. ")
        else:
            print(f"The number you chose is to low. You have {guesses} more attempts. Try again. ")

    else:
        print("--------------------------------------------------------------------")
        if guesses <= 0:
            print("You don't have any attempts left.")
        else:
            print("Congratulations you guessed the number.")
        while True:
            repeat = input("Do you want to play another round?(Y/N) ").lower()
            if repeat == "yes" or repeat == "y":
                print(".............Starting New Game..................")
                guesses = start_new_game()
                break

            elif repeat == "no" or repeat == "n":
                print("Have a nice day :)")
                print("...leaving game...")
                game_is_on = False
                break
            else:
                print(f'Sorry "{repeat}" is not an option. Can you repeat? ')





