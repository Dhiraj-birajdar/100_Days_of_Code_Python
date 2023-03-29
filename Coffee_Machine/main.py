MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

pay = 0
money = 0
change = 0


def update_report(cf):
    """ updates resources remaining and profit """
    global pay, money, change
    change = round(pay - MENU[cf]["cost"], 2)
    money += round(pay - change, 2)
    for i in resources:
        resources[i] -= MENU[cf]['ingredients'][i]


def req_check(cf, payment):
    """ accepts coffee name and payment and returns True if ingredients are available and payment is enough else returns
     false"""
    return MENU[cf]['cost'] <= payment and (resources["water"] >= MENU[cf]['ingredients']['water'] and resources["milk"] >= MENU[cf]['ingredients']['milk'] and resources["coffee"] >= MENU[cf]['ingredients']['coffee'])


def price():
    """ Calculates price and returns change or refund """
    print("Please enter coins.")
    qtr = int(input("How many Quarters? : "))
    dime = int(input("How many Dimes? : "))
    nickel = int(input("How many nickels? : "))
    penny = int(input("How many pennies? : "))
    return qtr * 0.25 + dime * 0.10 + nickel * 0.05 + penny * 0.01


while True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino) : ").lower()
    if choice == 'off':
        exit(0)
    elif choice == 'report':
        print("Water : ", resources["water"], 'ml')
        print("Milk : ", resources["milk"], 'ml')
        print("Coffee : ", resources["coffee"], 'g')
        print(f"Money : ${money}")
    elif choice == 'latte' or choice == 'espresso' or choice == 'cappuccino':
        pay = price()
        if req_check(choice, pay):
            update_report(choice)
            print(f"\nHere's your change : {change}")
            print(f"Here's your {choice}🍵. enjoy!😀")
        else:
            if not (MENU[choice]['cost'] <= pay):
                print("Money is not enough. Refunded.")
            else:
                for i in resources:
                    if resources[i] < MENU[choice]['ingredients'][i]:
                        print(f"Sorry there is not enough {i}")
                        break
            # elif not (resources["water"] >= MENU[choice]['ingredients']['water']):
            #     print("Sorry there is not enough water")
            # elif not (resources["milk"] >= MENU[choice]['ingredients']['milk']):
            #     print("Sorry there is not enough milk")
            # elif not (resources["coffee"] >= MENU[choice]['ingredients']["coffee"]):
            #     print("Sorry there is not enough coffee")
    else:
        print("Invalid choice!")
