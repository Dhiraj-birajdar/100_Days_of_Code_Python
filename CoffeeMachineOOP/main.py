from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
transaction = MoneyMachine()
machine = CoffeeMaker()

while True:
    choice = input(f"What do you like? {drinks.get_items()} : ").lower()
    if choice == 'report':
        machine.report()
        transaction.report()
    elif choice == 'off':
        exit(0)
    else:
        drink = drinks.find_drink(choice)
        if drink is None:
            pass
        elif machine.is_resource_sufficient(drink) and transaction.make_payment(drink.cost):
            machine.make_coffee(drink)

