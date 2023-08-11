from CoffeeMaker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


while True:
    # input the drink
    choice = input(f"Please select your drink: {menu.get_items()} ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        break
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"The price of one {drink.name} is {drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



