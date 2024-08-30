from random import choice

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeemachine_on = True
menu = Menu()
drinks = menu.get_items()
cof_maker = CoffeeMaker()
mon_mach = MoneyMachine()


while coffeemachine_on:
    choice_ = input(f"What would you like?: {drinks}")
    if choice_ == "report":
        cof_maker.report()
        mon_mach.report()

    elif choice_ == "off":

        break

    else:
        drink = menu.find_drink(choice_)
        if cof_maker.is_resource_sufficient(drink):
            if mon_mach.make_payment(drink.cost):
                cof_maker.make_coffee(drink)
