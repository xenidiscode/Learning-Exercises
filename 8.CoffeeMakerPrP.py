MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

def enough_money(keyword,money1):
    if money1 >= MENU[keyword]["cost"]:
        return True
    else:
        return False

def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes *  0.10 + nickels * 0.05 + pennies * 0.01


def report_():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: {money}$")

def profit():
        check1 = True
        while check1:
            money_ = insert_coins()
            if enough_money(choice_, money_):
                    change_ = money_ - MENU[choice_]["cost"]
                    if change_ > 0:
                        print(f"Here is ${change_} in change.")

                    if choice_ == "espresso":
                        print("Here is your espresso. Enjoy!")
                    elif choice_ == "capuccino":
                        print("Here is your cappucino. Enjoy!")
                    elif choice_ == "latte":
                        print("Here is your latte. Enjoy")

                    return MENU[choice_]["cost"]
            else:
                print("Sorry that's not enough money refunded.")

def enough_resources():
    temp=True
    for i in resources:
        if resources[i] < MENU[choice_]["ingredients"][i]:
            print(f"Sorry not enough {i}")
    if temp:
        return True
    else:
        return False

money=0
coffeemachine_on = True

while coffeemachine_on:
    choice_ = input("What would you like?: (espresso, latte, cappucino, report, off")
    if choice_ == "report":
        report_()

    elif choice_ == "espresso":
        if enough_resources():
            for i in resources:
               resources[i] -= MENU[choice_]["ingredients"][i]
            money += profit()

    elif choice_ == "latte":

        money += profit()
        for i in resources:
            resources[i] -= MENU[choice_]["ingredients"][i]

    elif choice_ == "capuccino":

        money += profit()
        for i in resources:
            resources[i] -= MENU[choice_]["ingredients"][i]

    elif choice_== "off":

        break