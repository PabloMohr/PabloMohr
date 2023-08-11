from cost_in_resources import coffee, resources
import time


def coffe_calculator():

    while True:

        insert_coins = int(input(f"Your choice is {coffee[select_coffee]['variety']}. "
                                 f"The price for your coffe is {coffee[select_coffee]['price']}€."
                                 f"\nPlease Insert Coins: "))

        if insert_coins < coffee[select_coffee]['price']:
            print(f"You inserted {insert_coins} but the price of the coffee is {coffee[select_coffee]['price']}.\n"
                  f"You need {coffee[select_coffee]['price'] - insert_coins}€ to be able to pick that coffee")

        elif insert_coins >= coffee[select_coffee]['price']:
            resources["money"] = resources["money"] + coffee[select_coffee]['price']  # Add money to the resource money
            for key, value in resources.items():  # Subtracting values of selected coffee from the resources
                for k, v in coffee[select_coffee].items():
                    if key == k:
                        resources[key] = value - v
        # Calculating if a resource is below 0
            insufficient_resources = [key for key, value in resources.items() if value < 0]
            if insufficient_resources:
                print(f"Sorry there is not enough {', '.join(insufficient_resources)} in the machine")
                break
            elif not insufficient_resources:
                print(f"Your exchange is: {insert_coins - coffee[select_coffee]['price']}€. Please take it.")
                print(f"Enjoy your {coffee[select_coffee]['variety']}!")
                time.sleep(5)
                print("\n-----------------------------------------------------------------------------------\n")
                break


while True:
    select_coffee = int(input(f"What kind of coffee do you want?\n"
                              f"Press:\n1) For Espresso.\n2) For Capuccino.\n3) For Milk Coffee\n"))
    if select_coffee == 1 or select_coffee == 2 or select_coffee == 3:
        coffe_calculator()
    elif select_coffee == 12:
        print("Admin code 12 entered...")
        resources["water"] += int(input(f"How much water do you want to fill? "))
        resources["milk"] += int(input(f"How much milk do you want to fill? "))
        resources["coffee"] += int(input(f"How much coffee do you want to fill? "))
        print(f"Filling finished... Your resources are now {resources}")
        time.sleep(5)
    elif select_coffee == 13:
        print("Admin code 13 entered...\n....Printing resources")
        print(resources)
        time.sleep(5)
    elif select_coffee == 23:
        print("Admin code 23 entered...\n ....Turning off...")
        time.sleep(2)
        print("Good Bye")
        break
    else:
        print(f"Sorry {select_coffee} is not an option.\nTry again.")
        print("-------------------------------------------------")
        time.sleep(3)
